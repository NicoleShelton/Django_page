from django.contrib import admin
from .models import Dress

# This registers the models for the admin site to create the inventory
admin.site.register(Dress)
