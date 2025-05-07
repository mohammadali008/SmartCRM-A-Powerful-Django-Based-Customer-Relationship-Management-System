from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import *
from order.models import *


# Define AddCustomer View
def AddCustomer(request):
	form = AddCustomerForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Record Added...")
				return redirect('home')
		return render(request, 'add_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')

# Define CustomerInfo
def CustomerInfo(request,pk):
	if request.user.is_authenticated:
		customer = Customer.objects.get(id=pk)
		orders = Order.objects.filter(customer_id=pk)
		# detail_order = orders.customer_set.all()
		# test = detail_order.myproduct.all()
# 		print(detail_order)
		context = {}
		context['customer'] = customer
		context['orders'] = orders
		return render(request,'info.html',context = context)







