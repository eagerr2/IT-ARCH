from django.shortcuts import render, redirect
from .models import Product

def home_view(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def login_view(request):
    return render(request, 'login.html')

def signup_view(request):
    return render(request, 'signup.html')

def shop_view(request, categorystr):
    productsbycategory = Product.objects.filter(category=categorystr)

    ctx = {
        'detail': categorystr,
        'productsbycategory': productsbycategory,
    }
    return render(request, 'shopbycategory.html', context=ctx)

def add_to_cart(request, product_id):
    
    product = Product.objects.get(id=product_id)

    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += 1
    else:
        cart[str(product_id)] = {
            'name': product.name,
            'price': float(product.price),
            'quantity': 1,
        }

    request.session['cart'] = cart

    return redirect('home')

def checkout_view(request):
    cart = request.session.get('cart', {})
    total = 0

    for product_id, item in cart.items():
        item['subtotal'] = item['price'] * item['quantity']
        total += item['subtotal']

    return render(request, 'checkout.html', {'cart': cart, 'total': total})

def clear_cart(request):
    request.session['cart'] = {}
    return redirect('home')