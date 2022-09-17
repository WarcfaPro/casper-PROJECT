from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('order', views.order, name='order'),
    path('account', views.account, name='account'),
    path('login', views.login, name='login'),
    path('registration', views.registration, name='reg'),

]