from django.db import models


class Basket(models.Model):
    product_name = models.CharField()
    product_price = models.FloatField()
    product_quantity = models.PositiveIntegerField()


class Customer(models.Model):
    id = models.PositiveIntegerField()
    name = models.CharField(max_length=100)
    registration_date = models.DateTimeField(auto_now_add=True)
    basket = models.OneToOneField(Basket, on_delete=models.CASCADE)
