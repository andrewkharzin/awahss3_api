from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from apps.users.models import User
from datetime import datetime
from django.utils import timezone

class FileAttachment(models.Model):
    file = models.FileField(upload_to='file_attachments/')
    note = models.ForeignKey('Note', on_delete=models.CASCADE, related_name='file_attachments')

    def __str__(self):
        return str(self.file)

class ImageAttachment(models.Model):
    image = models.ImageField(upload_to='image_attachments/')
    note = models.ForeignKey('Note', on_delete=models.CASCADE, related_name='image_attachments')

    def __str__(self):
        return str(self.image)
    

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Category(MPTTModel):
    name = models.CharField(max_length=100, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    icon = models.ImageField(upload_to='category_icons/', null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return f"{self.name}"

class Note(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag)  # Add this line to establish a ManyToMany relationship with tags.

    last_updated = models.DateTimeField(default=timezone.now)
    last_updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='updated_notes')

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        # Update the last_updated field with the current timestamp
        self.last_updated = timezone.now()

        super().save(*args, **kwargs)