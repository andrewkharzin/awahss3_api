from django.db.models.signals import pre_save
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import request
from django.contrib.auth.models import Group
from apps.companies.models import Company

@receiver(post_save, sender=Company)
def create_company_group(sender, instance, created, **kwargs):
    """
    A signal handler function that creates a new Group instance for a newly created Company instance.
    """
    if created:
        group_name = f'{instance.name} Group'
        new_group = Group.objects.create(name=group_name)
        instance.group = new_group
        instance.save()

