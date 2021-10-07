from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=20)
    picture = models.ImageField()
    address = models.CharField(max_length=100)
    postcode = models.CharField(max_length=10)
    link = models.URLField(max_length=100)
    schedule = models.DateTimeField()
