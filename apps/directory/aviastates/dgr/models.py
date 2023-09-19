from django.db import models
import os
from django.conf import settings
from django.utils.text import slugify
from django.utils.html import mark_safe


class BaseDG(models.Model):

    hazard_class = models.CharField(max_length=50, verbose_name='Hazard Class')
    reason_regulation = models.TextField(
        verbose_name='​Reason for Regulation', null=True, blank=True)
    description = models.TextField(
        verbose_name='Additional Information', null=True, blank=True)
    label = models.ImageField(upload_to='apps/aviastates/dgr/dangerous_goods_labels/',
                              verbose_name='Label Image', null=True, blank=True)

    @property
    def thumbnail_preview(self):
        if self.label:
            return mark_safe('<img src="{}" width="80" />'.format(self.label.url))
        return ""


class SubDivision(models.Model):
    subdivision_number = models.CharField(
        max_length=5, verbose_name='Sub-Division Number')
    description = models.CharField(max_length=255, verbose_name='Description')
    base_dg = models.ForeignKey(
        BaseDG, on_delete=models.CASCADE, related_name='subdivisions')
    label = models.ImageField(upload_to='apps/aviastates/dgr/dangerous_goods_labels/',
                              verbose_name='Label Image', null=True, blank=True)

    def __str__(self):
        return f'Sub-Division {self.subdivision_number}: {self.description}'


class DangerousGood(models.Model):
    UN_number = models.CharField(
        max_length=10, verbose_name='UN Number', null=True, blank=True)
    proper_shipping_name = models.CharField(
        max_length=255, verbose_name='Proper Shipping Name')
    hazard_class = models.CharField(max_length=10, verbose_name='Hazard Class')
    packing_group = models.CharField(
        max_length=5, verbose_name='Packing Group', null=True, blank=True)
    subsidiary_risk = models.CharField(
        max_length=10, verbose_name='Subsidiary Risk', null=True, blank=True)
    packing_instructions = models.TextField(
        verbose_name='Packing Instructions', null=True, blank=True)
    special_provisions = models.TextField(
        verbose_name='Special Provisions', null=True, blank=True)
    packaging_instructions = models.TextField(
        verbose_name='Packaging Instructions', null=True, blank=True)
    additional_information = models.TextField(
        verbose_name='Additional Information', null=True, blank=True)

    def __str__(self):
        return f'Dangerous Goods {self.UN_number}: {self.proper_shipping_name}'
