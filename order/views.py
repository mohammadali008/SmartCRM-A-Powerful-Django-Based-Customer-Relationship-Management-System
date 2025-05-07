from django.shortcuts import render,redirect
from django.contrib import messages
import order.models
from .forms import *
import pdfkit
from django.template.loader import get_template
import os
from django.http import HttpResponse
from .pdfmaker import *

# Define AddOrder View
def AddOrder(request):
	form = AddOrderForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_order = form.save()
				messages.success(request, "Record Added...")
				return redirect('home')
		return render(request, 'add_order.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')

# DefineAddToCart
def AddToCart(request):
	context = {}
	product_items = Products.objects.all()
	new_order = Order.objects.create(
		customer_id=1
	)

	return redirect('home')

# Define ViewOrder
def ViewPdf(requset,pk):
	context = {}
	current_order = Order.objects.get(id = pk)
	#Calculete variables
	order_total = 0
	if current_order:
		order_total = int(current_order.products.price)*int(current_order.amount)


	context['current_order'] = current_order
	context['include_products'] = current_order.products
	context['total_amount'] = "{: .2f}".format(order_total)
	# Options
	options = {
		'encoding': 'UTF-8',
		'javascript-delay': '10',  # Optional
		'enable-local-file-access': None,  # To be able to access CSS
		'page-size': 'A4',
		'custom-header': [
			('Accept-Encoding', 'gzip')
		],
	}

	# FieName of pdf

	fileName = '{}.pdf'.format(current_order.id)
	# HTML FIle to be converted to PDF - inside your Django directory
	template = get_template('order/pdf-template.html')
	# Render the HTML
	html = template.render(context)
	# Remember that location to wkhtmltopdf
	path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
	config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
	# Create the file
	file_content = pdfkit.from_string(html, False, configuration=config, options=options)
	# Create the HTTP Response
	response = HttpResponse(file_content, content_type='application/pdf')
	response['Content-Disposition'] = 'inline; filename = {}'.format(fileName)

	# Return
	return response

#
def pdf(request,pk):
	context = {}
	current_order = Order.objects.get(id=pk)
	# Calculete variables
	order_total = 0
	if current_order:
		order_total = int(current_order.products.price) * int(current_order.amount)

	context['current_order'] = current_order
	context['include_products'] = current_order.products
	context['total_amount'] = "{: .2f}".format(order_total)
	return pdf_convertor('order/pdf-template.html',context)


































