from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('shop/<str:categorystr>/', views.shop_view, name='shopbycategory'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('clear_cart/', views.clear_cart, name='clear_cart'),
]