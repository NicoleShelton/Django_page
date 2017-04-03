from django.db import models

class Dress(models.Model):
    name = models.CharField(max_length=20)
    quantity = models.IntegerField()
    price = models.IntegerField()
    description = models.CharField(max_length=100)
    img = models.CharField(max_length=100)

    def static_url(self):
        return "imgs/" + self.img

    def __str__(self):
        return self.name