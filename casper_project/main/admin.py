from django.contrib import admin
from .models import User, Order, Order_wait_list

# Register your models here.
admin.site.register(User)
admin.site.register(Order)
admin.site.register(Order_wait_list)
