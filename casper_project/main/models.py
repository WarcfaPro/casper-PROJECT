from __future__ import unicode_literals
from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from .managers import UserManager
from django.db import models
from django.contrib.auth.models import PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):
    company_type = models.CharField(max_length=10)
    company_name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(null=False, unique=True)
    phone = models.CharField(max_length=32, null=True, blank=True)
    inn = models.CharField(max_length=12, null=False, unique=True)
    data_registration = models.DateTimeField(auto_now_add=True)
    is_carrier = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    object = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


class Order(models.Model):
    company_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    company_name = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address_city = models.CharField(max_length=50)
    address_street = models.CharField(max_length=100)
    address_city_to = models.CharField(max_length=50)
    address_street_to = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    is_complete = models.BooleanField(default=False)
    is_payments = models.BooleanField(default=False)
    data = models.DateTimeField(auto_now_add=True)
    data_complete = models.DateTimeField(auto_now=True)
