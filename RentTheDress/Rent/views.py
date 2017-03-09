from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'Rent/home.html')

def inventory(request):
    return render(request, 'Rent/inventory.html')

def about(request):
    return render(request, 'Rent/about.html')