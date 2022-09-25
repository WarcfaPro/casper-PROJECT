from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('order', views.order, name='order'),
    path('account', views.account, name='account'),
    path('login', views.loginUser, name='login'),
    path('reg', views.register, name='register'),
    path('logout', views.logout_user, name='logout'),

]