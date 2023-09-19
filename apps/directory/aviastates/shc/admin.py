from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from apps.directory.aviastates.shc.models import SHC
from import_export import resources

# Register your models here.
class SHCResource(resources.ModelResource):
    class Meta:
        model = SHC
        fields = ('id', 'category', 'code', 'description',)


@admin.register(SHC)
class SHCAdmin(ImportExportModelAdmin):
    # resource_class = [AircraftResource]
    resource_class = SHCResource
    list_display = ('category',
                    'code', 'description',)
    list_filter = ('category',)
    search_fields = ('code',)