from import_export import resources
from .models import TouristAttraction

class TouristAttractionResource(resources.ModelResource):
    class Meta:
        model = TouristAttraction