from django.db import models
from django.contrib.auth.models import User


class Pizza(models.Model):

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Toping(models.Model):

    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Order(models.Model):

    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    size = models.CharField(max_length=10)
    sauce1 = models.CharField(max_length=10)
    sauce2 = models.CharField(max_length=10)
    deliver = models.CharField(max_length=10)
    date_order = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pizza.name} - {self.size},{self.sauce1},\
        {self.sauce2},{self.deliver} - {self.date_order}"