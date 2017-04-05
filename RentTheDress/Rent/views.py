from django.shortcuts import render, redirect
from django.contrib import messages
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
    if dress.quantity != 0:
        dress.quantity -= 1
        dress.save()
        messages.add_message(request, messages.SUCCESS, 'Sucessfully rented ' + dress.name + '!')
    elif dress.quantity == 0:
        messages.add_message(request, messages.WARNING, 'Sorry ' + dress.name + ' is out of stock!')
    return redirect('RentTheDress:inventory')

def returning(request, id):
    dress = Dress.objects.get(pk=id)
    if dress.quantity != 20:
        dress.quantity += 1
        dress.save()
        messages.add_message(request, messages.SUCCESS, 'Sucessfully returned ' + dress.name + '!')
    elif dress.quantity == 20:
        messages.add_message(request, messages.WARNING, 'Could not return ' + dress.name + ' item is fullly stocked!')
    return redirect('RentTheDress:inventory')
