from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    company_type_ = (('ИП', 'ИП'), ('ООО', 'ООО'))
    company_type = models.CharField(max_length=10, choices=company_type_, verbose_name='Типом организации')
    company_name = models.CharField(max_length=255, unique=True, verbose_name='Названием организации')
    email = models.EmailField(null=False, unique=True, verbose_name='Email')
    phone = models.CharField(max_length=32, null=True, blank=True, verbose_name='Телефоном')
    inn = models.CharField(max_length=12, null=False, unique=True, verbose_name='ИНН организации')
    data_registration = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')
    is_carrier = models.BooleanField(default=False, verbose_name='Перевозчик')
    is_active = models.BooleanField(default=True, verbose_name='Активен')
    is_staff = models.BooleanField(default=False, verbose_name='Сотрудник')
    is_superuser = models.BooleanField(default=False, verbose_name='Суперпользователь')
    is_verified = models.BooleanField(default=False, verbose_name='Верифицирован')

    object = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Order(models.Model):
    company_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_author')
    company_name = models.CharField(max_length=100)
    address_city = models.CharField(max_length=50)
    address_street = models.CharField(max_length=100)
    full_address = models.CharField(max_length=150)
    address_city_to = models.CharField(max_length=50)
    address_street_to = models.CharField(max_length=100)
    full_address_to = models.CharField(max_length=150)

    price = models.CharField(max_length=100)
    is_complete = models.BooleanField(default=False, blank=True, null=True)
    is_payments = models.BooleanField(default=False, blank=True, null=True)
    data = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    data_complete = models.DateTimeField(auto_now=True, blank=True, null=True)
