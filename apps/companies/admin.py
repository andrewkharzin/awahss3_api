from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.shortcuts import render
from django.utils.html import format_html
from apps.companies.company_instance.image import CompanyImage
from apps.companies.company_instance.document import CompanyDocument
from apps.companies.company_instance.event import CompanyEvent
from .models import Company

class CompanyDocumentInline(admin.TabularInline):
    model = CompanyDocument
    extra = 1

class CompanyImageInline(admin.TabularInline):
    model = CompanyImage
    extra = 1

class CompanyEventInline(admin.TabularInline):
    model = CompanyEvent
    extra = 1



class CompanyAdmin(admin.ModelAdmin):
    inlines = [CompanyDocumentInline, CompanyImageInline, CompanyEventInline]
    list_display = ('name', 'address', 'image_tag')
    list_filter = ('name',)
    search_fields = ('name', 'group__name', 'address')
    view_on_site = True

    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-height: 80px;" />'.format(obj.image.url))





admin.site.register(Company, CompanyAdmin)

