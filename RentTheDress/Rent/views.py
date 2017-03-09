from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'rent/home.html')

def inventory(request):
    return render(request, 'rent/inventory.html')

def about(request):
    return render(request, 'rent/about.html')