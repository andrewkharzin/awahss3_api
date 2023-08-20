from django.db import models
from django.contrib.auth.models import Group
from apps.users.models import User
from django.conf import settings
from django.utils import timezone
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=200)
    group = models.ForeignKey(Group, on_delete=models.PROTECT, editable=False, null=True)
    image = models.ImageField(upload_to='company_images')
    # users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='companies')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


    def delete(self, *args, **kwargs):
        group = self.group
        super().delete(*args, **kwargs)
        # Log deletion
        LogEntry.objects.log_action(
            user_id=self.pk,
            content_type_id=ContentType.objects.get_for_model(self).pk,
            object_id=self.pk,
            object_repr=self.__str__(),
            action_flag=DELETION,
            change_message='Deleted company {}'.format(self.__str__()),
        )
    
    class Meta:
        verbose_name_plural = 'Companies'
        ordering = ('name',)


class CompanyPhone(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='phones')
    phone = models.CharField(max_length=20)
    contact_person = models.CharField(max_length=155, blank=True, null=True, default="")

    def __str__(self):
        return self.phone
    

    


