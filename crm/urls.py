from django.contrib import admin
from django.urls import path
# Import my Views
from .view import *
from customer.views import *
from order.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home,name = 'home'),
    path('add-customer',AddCustomer,name = 'add_record'),
    path('add-order',AddOrder,name = 'add_order'),
    path('customer/<int:pk>',CustomerInfo,name = 'customer_info'),
    path('test/<int:pk>',pdf,name = 'add_to_cart'),
]
