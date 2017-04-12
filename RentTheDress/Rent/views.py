from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Dress

# This is the request for the home page
def home(request):
    return render(request, 'rent/home.html')

# This is the request for the inventory page 
def inventory(request):
    dresses = Dress.objects.all()
    return render(request, 'rent/inventory.html', {'dresses': dresses})

# This is the request for the about page
def about(request):
    return render(request, 'rent/about.html')

# This is the function that allows the user to rent a dress
def renting(request, id):
    dress = Dress.objects.get(pk=id)
    # This says that if the items in stock is more than 0 the user can rent a dress
    if dress.quantity != 0:
        dress.quantity -= 1
        # This saves to the database so when you refresh the page the dress is still removed
        dress.save()
        # This is the sucess message the user recieves when they successfully rent a dress
        messages.add_message(request, messages.SUCCESS, 'Sucessfully rented ' + dress.name + '!')
    # This says if the stock is 0 they can't rent a dress
    elif dress.quantity == 0:
        # This is the warning message the user recieves when they are not able rent a dress
        messages.add_message(request, messages.WARNING, 'Sorry ' + dress.name + ' is out of stock!')
    return redirect('RentTheDress:inventory')

# This is the function that allows the user to return a dress
def returning(request, id):
    dress = Dress.objects.get(pk=id)
    # This is saying that if the quantity is not 20 the user can return a dress
    if dress.quantity != 20:
        dress.quantity += 1
        # This saves to the database so when you refresh the page the dress stays instock
        dress.save()
        # This is the sucess message letting the user know they successfully returned the dress
        messages.add_message(request, messages.SUCCESS, 'Sucessfully returned ' + dress.name + '!')
        # This says if the stock is 20 the user can't return a dress
    elif dress.quantity == 20:
        # This is the warning message letting the user know the stock is full
        messages.add_message(request, messages.WARNING, 'Could not return ' + dress.name + ' item is fullly stocked!')
    return redirect('RentTheDress:inventory')
