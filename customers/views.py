from django.shortcuts import render
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Customer, Basket


@receiver(post_save, sender=Customer)
def create_basket(sender, instance, created, **kwargs):
    if created:
        Basket.objects.create(customer=instance)


def produce_customer(request):
    if request.method == "POST":
        customer = Customer.objects.create(name="New Customer")
        customer.save()
        return render(request, 'produce_customer_success.html')
