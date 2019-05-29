from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Regular_pizza(models.Model):
    category = models.CharField(max_length=64, default='Regular Pizza')
    name = models.CharField(max_length=64)
    small = models.DecimalField(max_digits=4, decimal_places=2)
    large = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.category} - {self.name} - {self.small} - {self.large}"

class Sicilian_pizza(models.Model):
    category = models.CharField(max_length=64, default='Sicilian Pizza')
    name = models.CharField(max_length=64)
    small = models.DecimalField(max_digits=4, decimal_places=2)
    large = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.category} - {self.name} - {self.small} - {self.large}"

class Topping(models.Model):
    category = models.CharField(max_length=64, default='Only for Pizza')
    name = models.CharField(max_length=64)
    normal = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.category} - {self.name} - {self.normal}"

class Sub(models.Model):
    category = models.CharField(max_length=64, default='Sub')
    name = models.CharField(max_length=64)
    small = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    large = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.category} - {self.name} - {self.small} - {self.large}"

class Pasta(models.Model):
    category = models.CharField(max_length=64, default='Pasta')
    name = models.CharField(max_length=64)
    normal = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.category} - {self.name} - {self.normal}"

class Salad(models.Model):
    category = models.CharField(max_length=64, default='Salad')
    name = models.CharField(max_length=64)
    normal = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.category} - {self.name} - {self.normal}"

class Dinner_platter(models.Model):
    category = models.CharField(max_length=64, default='Dinner Platter')
    name = models.CharField(max_length=64)
    small = models.DecimalField(max_digits=4, decimal_places=2)
    large = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.category} - {self.name} - {self.small} - {self.large}"

class Order_counter(models.Model):
    counter = models.IntegerField()

    def __str__(self):
        return f"Order no: {self.counter}"

class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class User_order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_number = models.IntegerField()
    topping_allowance = models.IntegerField(default=0)
    status = models.CharField(max_length=64, default='initiated')

    def __str__(self):
        return f"{self.user} - {self.order_number} - {self.status} Topping_allowance: {self.topping_allowance}"

class Order2(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.IntegerField()
    category = models.CharField(max_length=64, null=True)
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.category} - {self.name} - ${self.price}"
