from django.core.management.base import BaseCommand
from attraction.models import TouristAttraction

class Command(BaseCommand):
    help = 'Deletes all TouristAttraction objects'

    def handle(self, *args, **kwargs):
        TouristAttraction.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted all tourist attractions.'))
