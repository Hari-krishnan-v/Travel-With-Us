import csv
from django.core.management.base import BaseCommand
from attraction.models import TouristAttraction
import logging


class Command(BaseCommand):
    help = 'Imports tourist attractions from a CSV file'

    def add_arguments(self, parser):
        # Add a command-line argument to specify the CSV file
        parser.add_argument('Top_Indian_Places_to_Visit.csv', type=str,help='TravelWithUs/attraction/Top_Indian_Places_to_Visit.csv')

    def handle(self, *args, **options):
        csv_file_path = options['Top_Indian_Places_to_Visit.csv']

        try:
            with open(csv_file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)

                # Loop through each row in the CSV
                for row in reader:
                    # Debugging: Print the row to help identify potential issues
                    print(f"Processing row: {row}")

                    # Validate and extract data for each row
                    try:
                        # Ensure required fields are not empty
                        if not row['Zone'] or not row['State'] or not row['City'] or not row['Name']:
                            self.stdout.write(self.style.WARNING(f"Missing mandatory fields in row: {row}"))
                            continue

                        # Handle missing or malformed data gracefully
                        establishment_year = self.safe_int(row['Establishment Year'])
                        time_needed_in_hrs = self.safe_float(row['time needed to visit in hrs'])
                        google_review_rating = self.safe_float(row['Google review rating'])
                        entrance_fee_in_inr = self.safe_int(row['Entrance Fee in INR'])
                        google_reviews_in_lakhs = self.safe_float(row['Number of google review in lakhs'])

                        # Check for empty strings and handle them for optional fields
                        weekly_off = row['Weekly Off'] if row['Weekly Off'] else None
                        dslr_allowed = row['DSLR Allowed'].lower() == 'yes' if row['DSLR Allowed'] else False
                        best_time_to_visit = row['Best Time to visit']

                        # Create the TouristAttraction object
                        attraction = TouristAttraction(
                            zone=row['Zone'],
                            state=row['State'],
                            city=row['City'],
                            name=row['Name'],
                            attraction_type=row['Type'],
                            establishment_year=establishment_year,
                            time_needed_in_hrs=time_needed_in_hrs,
                            google_review_rating=google_review_rating,
                            entrance_fee_in_inr=entrance_fee_in_inr,
                            nearest_airport=row['Airport with 50km Radius'],
                            weekly_off=weekly_off,
                            significance=row['Significance'],
                            dslr_allowed=dslr_allowed,
                            google_reviews_in_lakhs=google_reviews_in_lakhs,
                            best_time_to_visit=best_time_to_visit
                        )

                        # Save the object to the database
                        attraction.save()
                        self.stdout.write(self.style.SUCCESS(f"Successfully imported: {row['Name']}"))

                    except Exception as e:
                        # Log the error if any field is invalid or cannot be processed
                        self.stdout.write(self.style.ERROR(f"Error importing row: {row['Name']} - {str(e)}"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error opening the CSV file: {e}"))

    def safe_int(self, value):
        """Safely converts a value to an integer or returns None if invalid."""
        try:
            return int(value) if value else None
        except ValueError:
            return None

    def safe_float(self, value):
        """Safely converts a value to a float or returns None if invalid."""
        try:
            return float(value) if value else None
        except ValueError:
            return None
