from django.db import models

# Create your models here.
class Dress(models.Model):
    dress = models.CharField(max_length=20)
    quantity = models.IntegerField()
    image = models.URLField()
    price = models.IntegerField()
    description = models.CharField(max_length=50)