from django.shortcuts import render, redirect
from .models import Dress

def home(request):
    return render(request, 'rent/home.html')

def inventory(request):
    dresses = Dress.objects.all()
    return render(request, 'rent/inventory.html', {'dresses': dresses})

def about(request):
    return render(request, 'rent/about.html')

def renting(request, id):
    dress = Dress.objects.get(pk=id)
    dress.quantity -= 1
    dress.save()
    return redirect('RentTheDress:inventory')

def returning(request, id):
    dress = Dress.objects.get(pk=id)
    dress.quantity += 1
    dress.save()
    return redirect('RentTheDress:inventory')
