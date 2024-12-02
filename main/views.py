from django.shortcuts import render
from .models import Product

def home_view(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def login_view(request):
    return render(request, 'login.html')

def signup_view(request):
    return render(request, 'signup.html')

def checkout_view(request):
    return render(request, 'checkout.html')

def shop_view(request, detail):

    ctx = {
        'detail' : detail,
    }
    return render(request, 'shop.html', context=ctx)