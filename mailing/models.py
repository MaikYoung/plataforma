from django.db import models


class Contact(models.Model):
    name = models.CharField(blank=True, max_length=250)
    number = models.CharField(blank=True, max_length=250)
    address = models.CharField(blank=True, max_length=250)
    text = models.CharField(blank=True, max_length=250)
    create_at = models.DateTimeField(auto_now_add=True)
