from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import DangerousGood, SubDivision, BaseDG

# Define a resource for DangerousGoods for import/export


class DGResource(resources.ModelResource):
    class Meta:
        model = BaseDG
        fields = ('id', 'hazard_class', 'reason_regulation', 'description',)


# Inline for SubDivision
class SubDivisionInline(admin.TabularInline):
    model = SubDivision
    extra = 1


@admin.register(BaseDG)
class AdminDG(ImportExportModelAdmin):
    resource_class = DGResource
    list_display = ('hazard_class', 'thumbnail_preview')
    inlines = [SubDivisionInline]

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Label Preview'
    thumbnail_preview.allow_tags = True

# Define a resource for DangerousGoods for import/export


class DangerousGoodsResource(resources.ModelResource):
    class Meta:
        model = DangerousGood
        fields = ('id', 'UN_number', 'proper_shipping_name',
                  'hazard_class', 'packing_group', 'subsidiary_risk',)


@admin.register(DangerousGood)
class DangerousGoodsAdmin(ImportExportModelAdmin):
    resource_class = DangerousGoodsResource
    list_display = ('UN_number', 'proper_shipping_name',
                    'hazard_class', 'packing_group', 'subsidiary_risk')
    search_fields = ('UN_number', 'proper_shipping_name', 'hazard_class')

# Register SubDivision model separately if needed
# admin.site.register(SubDivision)
