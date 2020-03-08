from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create the items on the menu.
class RegularPizza(models.Model):
    name = models.CharField(max_length=64)
    small_price = models.DecimalField(max_digits=4, decimal_places=2)
    large_price = models.DecimalField(max_digits=4, decimal_places=2)
        
    def __str__(self):
        return f"{self.name} - €{self.small_price} | €{self.large_price}"

class SicilianPizza(models.Model):
    name = models.CharField(max_length=64)
    small_price = models.DecimalField(max_digits=4, decimal_places=2)
    large_price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name} - €{self.small_price} | €{self.large_price}"

class Topping(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name}"

class Sub(models.Model):
    name = models.CharField(max_length=64)
    small_price = models.DecimalField(max_digits=4, decimal_places=2)
    large_price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name} - €{self.small_price} | €{self.large_price}"

class Addition(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name}"

class Pasta(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name} - €{self.price}"

class Salad(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name} - €{self.price}"

class Dinnerplatter(models.Model):
    name = models.CharField(max_length=64)
    small_price = models.DecimalField(max_digits=4, decimal_places=2)
    large_price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name} - €{self.small_price} | €{self.large_price}"

# Create the orders.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_number = models.IntegerField()
    date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=30, default='unpaid')
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Order number: {self.order_number} - ordered on {self.date} by {self.user} - status: {self.status}"

class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_number = models.IntegerField()
    category = models.CharField(max_length=64, default ='-')
    item = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"Order {self.order_number} | {self.category} {self.item} - €{self.price}"

class Count(models.Model):
    counter = models.IntegerField()

    def __str__(self):
        return f"Order number: {self.counter}"