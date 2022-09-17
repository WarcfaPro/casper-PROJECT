from django.db import models


class Order(models.Model):
    client_id = models.PositiveIntegerField()
    address_city = models.CharField(max_length=50)
    address_street = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    is_complete = models.BooleanField(default=False)
    data = models.DateTimeField(auto_now_add=True)
    data_complete = models.DateTimeField(auto_now=True)
