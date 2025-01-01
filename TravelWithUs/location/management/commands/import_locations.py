# location/management/commands/import_locations.py
import csv
import os
from django.core.management.base import BaseCommand
from location.models import Location

class Command(BaseCommand):
    help = 'Imports location data from a CSV file into the Location model'

    def add_arguments(self, parser):
        # Allow specifying the CSV file path as an argument
        parser.add_argument(
            'worldcities.csv',
            type=str,
            help='TravelWithUs/location/worldcities.csv'
        )

    def handle(self, *args, **kwargs):
        csv_file = kwargs['worldcities.csv']

        # Ensure the file exists
        if not os.path.isfile(csv_file):
            self.stdout.write(self.style.ERROR(f'File "{csv_file}" not found.'))
            return

        try:
            with open(csv_file, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        # Create a Location instance and save it to the database
                        location = Location(
                            city=row['city'],
                            city_ascii=row['city_ascii'],
                            lat=float(row['lat']),
                            lng=float(row['lng']),
                            country=row['country'],
                            iso2=row['iso2'],
                            iso3=row['iso3'],
                            admin_name=row['admin_name'],
                            capital=row['capital'],
                            population=int(row['population']),
                            city_id=int(row['id'])
                        )
                        location.save()
                        self.stdout.write(self.style.SUCCESS(f'Successfully added {location.city}'))
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(f'Error adding {row["city"]}: {e}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error opening the file: {e}'))
