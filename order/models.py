from django.contrib.auth.models import User
from django.db import models
from customer.models import Customer
from products.models import Products

# DEfine Order Model

class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    date = models.DateField(verbose_name = "تاریخ صدور",blank=True,null=True)
    products = models.ForeignKey(Products,null=True,on_delete=models.CASCADE,related_name='myproduct')
    amount = models.IntegerField(verbose_name='تعدادکارتن',blank=True,null=True)
    total = models.IntegerField(verbose_name='تعدادکل',blank=True,null=True)
    total_of_price = models.IntegerField(verbose_name='قیمت کل')

    def __str__(self):
        return f"{self.customer.first_name} {self.customer.last_name}\n{self.date}"

    def create_items(self):
        list_of = ()
        products = Products.objects.all()
        for item in products:
            pass


# Define OrderDetail
class OrderDetail(models.Model):
    current_order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='current_order')
    current_products = models.ForeignKey(Products,on_delete=models.CASCADE,related_name='current_products')
    final_price = models.IntegerField(null=True,blank=True)
    count = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return str(self.current_order)



















