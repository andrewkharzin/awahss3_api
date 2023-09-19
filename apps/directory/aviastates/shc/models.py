from django.db import models


class SHC(models.Model):
    code = models.CharField(max_length=10, unique=False)
    description = models.TextField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.code
