from django.conf import settings
from django.db import models


class Order(models.Model):
    company_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company_type = models.CharField(max_length=10)
    company_name = models.CharField(max_length=100)
    client_number = models.PositiveIntegerField()
    address_city = models.CharField(max_length=50)
    address_street = models.CharField(max_length=100)
    address_city_to = models.CharField(max_length=50)
    address_street_to = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    is_complete = models.BooleanField(default=False)
    is_payments = models.BooleanField(default=False)
    data = models.DateTimeField(auto_now_add=True)
    data_complete = models.DateTimeField(auto_now=True)
