from django.db import models
from apps.companies.models import Company

class CompanyImage(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='images')
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='company_images')

    def __str__(self):
        return self.name