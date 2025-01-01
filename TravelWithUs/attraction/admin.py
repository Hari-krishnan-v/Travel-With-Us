from django.contrib import admin
from .models import Attraction,TouristAttraction
from import_export.admin import ExportMixin, ImportExportModelAdmin
from .resources import TouristAttractionResource
# Register your models here.


admin.site.register(Attraction)

@admin.register(TouristAttraction)
class TouristAttractionAdmin(admin.ModelAdmin):
    actions = ['delete_all_tourist_attractions']

    def delete_all_tourist_attractions(self, request, queryset):
        queryset.delete()
        self.message_user(request, "All tourist attractions have been deleted.")

    delete_all_tourist_attractions.short_description = "Delete all tourist attractions"




