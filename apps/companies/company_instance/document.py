from django.db import models
import datetime
from apps.companies.models import Company

def upload_document_path(instance, filename):
    # Get the group name of the company associated with the document
    group_name = instance.company.group.name

    # Format the upload path using the group name, upload date, and original filename
    upload_date = datetime.date.today().strftime('%Y-%m-%d')
    upload_path = f"{group_name}/documents/{upload_date}/{filename}"

    return upload_path

class CompanyDocument(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='documents')
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to=upload_document_path, null=True, blank=True)

    def __str__(self):
        return self.name
    
