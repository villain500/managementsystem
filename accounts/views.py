from django.shortcuts import render,redirect
from django.http import HttpResponse
from accounts.models import Product,Customer,Order
from .form import OrderForm,Createuser
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user,allowed_users,admin_only
from django.contrib.auth.models import Group

# Create your views here.
@login_required(login_url='login')
def userprofile(request):
    return render(request, 'userprofile.html')
@login_required(login_url='login')
@admin_only
def home(request):
    order=Order.objects.all()
    customers=Customer.objects.all()
    total_customers=customers.count()
    total_orders=order.count()
    total_delivered=order.filter(status='Delivered').count()
    data={
        'order':order,
        'customers':customers,
        'total_customers':total_customers,
        'total_orders':total_orders,
        'total_delivered':total_delivered
    }
    return render(request,'dashboard.html',data)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def products(request):
    products=Product.objects.all()
    return render(request,'product.html',{'products':products})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customers(request,pk_id):
    
    customer=Customer.objects.get(id=pk_id)
    orders=customer.order_set.all()
    order_count=orders.count()
    data={
        'customer':customer,
        'orders':orders,
        'order_count':order_count
    }
    return render(request,'customer.html',data)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def create_order(request,pk):
    customer=Customer.objects.get(id=pk)
    form=OrderForm(initial={'customer':customer})
    if request.method== 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'create_order.html',{'form':form})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def update_order(request,pk):
    order=Order.objects.get(id=pk)
    form=OrderForm(instance=order)
    if request.method== 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'update_order.html',{'form':form})



@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def delete_order(request,pk):
    order=Order.objects.get(id=pk)
    if request.method=='POST':
        order.delete()
        return redirect('home')
    return render(request, 'delete_order.html')

@unauthenticated_user
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form=Createuser()
        if request.method=='POST':
            form=Createuser(request.POST)
            if form.is_valid:
                user = form.save()
                # username = form.cleaned_data.get('username')
                group=Group.objects.get(name='customer')
                user.groups.add(group)
                
                return redirect('login')
        data={'form':form}
        return render(request, 'register.html',data)

@unauthenticated_user
def login_here(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user = authenticate(username=username,password=password)
            print(user)
            if user is not None:
                login(request, user)
                messages.success(request,'log in success')
                return redirect('home')
        return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('login')

