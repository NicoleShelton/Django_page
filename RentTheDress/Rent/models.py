from django.db import models

class Dress(models.Model):
    name = models.CharField(max_length=20)
    quantity = models.IntegerField()
    image = models.URLField()
    price = models.IntegerField()
    description = models.CharField(max_length=100)