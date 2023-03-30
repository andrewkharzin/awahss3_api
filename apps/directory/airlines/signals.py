import os
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.directory.airlines.models.airline import Airline

@receiver(post_save, sender=Airline)
def link_image_to_airline(sender, instance, created, **kwargs):
    if created:
        # Get the list of files in the "airlines/" directory
        image_files = os.listdir("media/airlines/square/")
        
        # Find the image file that matches the Airline name
        for filename in image_files:
            if filename.startswith(instance.codeIataAirline):
                # If a matching image file is found, link it to the Airline instance
                instance.arl_logo = "airlines/square/" + filename
                instance.save()
                break

@receiver(post_save, sender=Airline)
def link_image_to_countries(sender, instance, created, **kwargs):
    if created:
        # Get the list of files in the "airlines/" directory
        image_files = os.listdir("media/countries/logos/")
        
        # Find the image file that matches the Airline name
        for filename in image_files:
            if filename.startswith(instance.nameCountry):
                # If a matching image file is found, link it to the Airline instance
                instance.cntr_logo = "countries/logos/" + filename
                instance.save()
                break