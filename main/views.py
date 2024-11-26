from django.shortcuts import render
from .models import Product

def home_view(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def login_view(request):
    pass

def signup_view(request):
    pass

def checkout_view(request):
    pass