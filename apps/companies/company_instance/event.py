from django.db import models
from apps.companies.models import Company

class CompanyEvent(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='events')
    name = models.CharField(max_length=100)
    date = models.DateTimeField()

    def __str__(self):
        return self.name