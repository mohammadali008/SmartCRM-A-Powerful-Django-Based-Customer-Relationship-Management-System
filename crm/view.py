from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from customer.models import Customer

# Define HomePage
def Home(request):
    customers = Customer.objects.all().order_by('-id')
    context = {'customers':customers}
    # Check User Login
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
            request,
            username = username,
            password = password
        )
        if user is not None:
            login(request,user)
            messages.success(request,'Ok')
            print("oooo")
            return redirect('home')
        else:
            messages.success(request,'No')
            print('nonono')
            return redirect('home')
    else:
        return render(request,'home.html',context = context)





















