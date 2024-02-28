from django.shortcuts import render , redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms


def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request,'product.html', {'product':product})



def index(request):
    products = Product.objects.all()
    return render(request,'index.html', {'products':products})

def contact(request):
    return render(request,'contact.html', {})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'شما با موفقیت وارد شدید')
            return redirect('index')
        else:
            messages.error(request, 'نام کاربری یا رمز عبور اشتباه است')
            return redirect('login')
    else:
        return render(request,'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, 'شما از حساب کاربری خود خارج شدید')
    return redirect('index')

def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Check if username or email already exists
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            form.save()
            # Login user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'حساب کاربری شما با موفقیت ساخته شد!')
            return redirect('index')
        else:
            messages.error(request, 'نام کاربری قابل استفاده نیست')
            return render(request, 'register.html', {'form': form})


    else:
        return render(request,'register.html', {'form':form})
    


