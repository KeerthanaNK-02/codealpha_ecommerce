from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Product, Order


# HOME PAGE
def store(request):

    products = Product.objects.all()

    return render(request, 'store/store.html', {
        'products': products
    })


# PRODUCT DETAIL PAGE
def product_detail(request, id):

    product = Product.objects.get(id=id)

    return render(request, 'store/product_detail.html', {
        'product': product
    })


# CART PAGE
def cart(request):

    return render(request, 'store/cart.html')


# CHECKOUT PAGE
def checkout(request):

    if not request.user.is_authenticated:

        return redirect('/login/')

    if request.method == "POST":

        name = request.POST.get('name')
        address = request.POST.get('address')
        items = request.POST.get('items')
        total = request.POST.get('total')

        # SAVE ORDER
        Order.objects.create(
            user=request.user,
            name=name,
            address=address,
            items=items,
            total=total
        )

        return render(request, 'store/success.html')

    return render(request, 'store/checkout.html')


# MY ORDERS PAGE
def my_orders(request):

    if request.user.is_authenticated:

        orders = Order.objects.filter(
            user=request.user
        ).order_by('-created_at')

    else:

        orders = []

    return render(request, 'store/my_orders.html', {
        'orders': orders
    })


# LOGIN PAGE
def login_view(request):

    error = ""

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return render(request, 'store/login_success.html', {
                'message': 'Login Successful!'
            })

        else:

            error = "Invalid Username or Password"

    return render(request, 'store/login.html', {
        'error': error
    })


# LOGOUT
def logout_view(request):

    logout(request)

    return redirect('/')


# REGISTER PAGE
def register(request):

    error = ""

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        # CHECK USERNAME
        if User.objects.filter(username=username).exists():

            error = "Username already exists"

        else:

            User.objects.create_user(
                username=username,
                password=password
            )

            return render(request, 'store/register_success.html', {
                'message': 'Registration Successful!'
            })

    return render(request, 'store/register.html', {
        'error': error
    })


# WISHLIST PAGE
def wishlist(request):

    return render(request, 'store/wishlist.html')