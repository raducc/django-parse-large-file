from django.db import models

__all__ = ['Customer']


class Customer(models.Model):
    email = models.EmailField(unique=True)
    age = models.SmallIntegerField(null=True, blank=True)
    added_at = models.DateField(auto_now_add=True)
    last_seen = models.DateField(null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
