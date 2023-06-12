from django.urls import path
from .views import produce_customer


urlpatterns = [
    path('produce_customer/', produce_customer, name='produce-customer'),
]
