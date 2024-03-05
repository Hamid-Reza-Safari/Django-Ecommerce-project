from math import e
from django.shortcuts import render , redirect
from .models import Category, Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms


def category(request, foo):
    # remove spaces (if there is any)
    foo = foo.replace('-', ' ')
    # grab category from name
    try:
        # look up the category
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        # Setting active page as 'category' and category_name as foo
        return render(request, 'category.html', {'products': products, 'category': category, 'active_page': 'category', 'category_name': foo}) 
    except Category.DoesNotExist:
        messages.error(request, 'دسته بندی مورد نظر یافت نشد')
        return redirect('index')

def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request,'product.html', {'product':product})



def index(request):
    products = Product.objects.all()
    return render(request,'index.html', {'products': products, 'active_page': 'index'})

def contact(request):
    return render(request,'contact.html', {'active_page': 'contact'})

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
            # Save the form to create the user
            form.save()
            # Extract username and password
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # login the user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'حساب کاربری شما با موفقیت ساخته شد!')
            return redirect('index')
        else:
            # Debugging: Print form errors
            print(form.errors)
            if 'username' in form.errors:
                messages.error(request, 'نام کاربری تکراری است .')
            if 'password2' in form.errors:
                password_errors = form.errors['password2']
                for error in password_errors:
                    # Check for specific error messages in English and convert them to Persian
                    if 'match' in error:
                        messages.error(request, 'رمز های عبور با هم مطابقت ندارند.')
                    elif 'short' in error:
                        messages.error(request, 'رمز عبور باید حداقل ۸ کاراکتر داشته باشد.')
                    elif 'common' in error:
                        messages.error(request, 'این رمز عبور بسیار ساده است.')
                    elif 'numeric' in error:
                        messages.error(request, 'این رمز فقط شامل اعداد است لطفا از کلمات نیز استفاده کنید')

            # If form is not valid, display error message and return with the form
            return render(request, 'register.html', {'form': form})
    else :
        # Debugging: Print GET request
        print("GET request received")
        # If it's a GET request or form is not valid, render the form
        return render(request,'register.html', {'form': form})


def forget_password(request):
    return render(request,'forget.html', {})






def offer_page(request):
    products = Product.objects.filter()
    category = Category.objects.get
    return render(request,'offer.html', {'products': products,'active_page': 'offer' , 'category': category})


