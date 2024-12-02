from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('shop/<str:detail>', views.shop_view, name='shop'),
]

