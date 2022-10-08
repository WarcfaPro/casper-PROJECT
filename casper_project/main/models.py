from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
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
    email_verified = models.BooleanField(default=False, verbose_name='Верификация email')

    object = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Order(models.Model):
    company = models.ForeignKey(User, on_delete=models.PROTECT, related_name='order_author')
    company_name = models.CharField(max_length=100)
    address_city = models.CharField(max_length=50)
    address_street = models.CharField(max_length=100, blank=True, null=True)
    full_address = models.CharField(max_length=150)
    address_city_to = models.CharField(max_length=50)
    address_street_to = models.CharField(max_length=100, blank=True, null=True)
    full_address_to = models.CharField(max_length=150)
    price = models.DecimalField(verbose_name='Стоимость', max_digits=19, decimal_places=0, blank=True, null=True)
    carrier = models.ForeignKey('Order_wait_list', on_delete=models.SET_NULL, related_name='order_carrier',
                                   blank=True, null=True,)
    is_complete = models.BooleanField(default=False, blank=True, null=True)
    is_payments = models.BooleanField(default=False, blank=True, null=True)
    data = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    data_update = models.DateTimeField(auto_now=True, blank=True, null=True)
    is_hidden = models.BooleanField(default=False, verbose_name='Скрыт от пользователя (думает что удален!)')

    def __str__(self):
        return f'{self.id}'


class Order_wait_list(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ', related_name='order_in_w_list')
    carrier = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Доставщик', related_name='carrier_order')
    carrier_price = models.DecimalField(verbose_name='Стоимость', max_digits=19, decimal_places=0)
    data_add_to_wait_list = models.DateTimeField(verbose_name='Дата создания заявки', auto_now_add=True)
    is_selected = models.BooleanField(default=False, verbose_name='Выбрана заказчиком')

    def __str__(self):
        return f'{self.carrier}'
