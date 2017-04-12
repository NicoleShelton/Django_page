from django.db import models

# This is all the information the database is keeping up with
class Dress(models.Model):
    name = models.CharField(max_length=20)
    quantity = models.IntegerField()
    price = models.IntegerField()
    description = models.CharField(max_length=100)
    img = models.CharField(max_length=100)

    # This is the function for the  images to be viewed
    def static_url(self):
        return "imgs/" + self.img

    def __str__(self):
        return self.name