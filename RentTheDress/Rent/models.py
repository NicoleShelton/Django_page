from django.db import models

<<<<<<< HEAD
# Create your models here.
=======
>>>>>>> 63c748ed145b3ce8a6432fffe3db8708cbcf0f05
class Dress(models.Model):
    dress = models.CharField(max_length=20)
    quantity = models.IntegerField()
    image = models.URLField()
    price = models.IntegerField()
<<<<<<< HEAD
    description = models.CharField(max_length=50)
=======
    description = models.CharField(max_length=50)
>>>>>>> 63c748ed145b3ce8a6432fffe3db8708cbcf0f05
