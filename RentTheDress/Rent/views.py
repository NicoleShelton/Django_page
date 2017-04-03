from django.shortcuts import render, redirect
from .models import Dress

def home(request):
    return render(request, 'rent/home.html')

def inventory(request):
    dress = Dress.objects.all()
    return render(request, 'rent/inventory.html')

def about(request):
    return render(request, 'rent/about.html')

def rent(request, id, quan):
    dress = Dress.objects.get(pk=id)
    dress.quantity -= quan
    dress.save()
    return render(request, 'rent/home.html')
