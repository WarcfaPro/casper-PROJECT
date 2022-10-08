from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('order', views.order, name='order'),
    path('account', views.account, name='account'),
    path('login', views.loginUser, name='login'),
    path('reg', views.register, name='register'),
    path('logout', views.logout_user, name='logout'),
    path('order/list', views.order_list, name='order_list'),
    path('account/change', views.account_dc, name='account_dc'),
    path('account/order', views.your_order_list, name='y_o_l'),
    path('account/order/<order_id>', views.order_detail, name='order_detail'),

]