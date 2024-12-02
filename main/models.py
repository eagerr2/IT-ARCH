from django.db import models
from django.contrib.auth.models import User


#for the home page
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='static/css/images')
    description = models.TextField()
    CATEGORY_CHOICES = [('Home Appliances', 'Home Appliances'), 
                        ('TV & Audio', 'TV & Audio'), 
                        ('Small Appliances', 'Small Appliances'), 
                        ('Computing & Gaming', 'Computing & Gaming'), 
                        ('Smart devices', 'Smart devices'), 
                        ]

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f'{self.name}: €{self.price}'
    
#for the shopping cart
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product}: {self.quantity}'

#for the checkout process
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_address = models.TextField()
    delivery_option = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'€{self.total_cost}'
