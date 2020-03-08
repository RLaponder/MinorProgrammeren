from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from .models import *
from decimal import Decimal

# Set counter for the order numbers.
counter = Count.objects.first()
if counter == None:
    set_counter = Count(counter=1)
    set_counter.save()

def index(request):
    # Show the login page if a user is not logged in.
    if not request.user.is_authenticated:
        context = {
            "loggedin": False
        }
        return render(request, "users/login.html", context)

    # Show index page if a user is logged in.
    context = {
        "user": request.user,
        "loggedin": True
    }
    return render(request, "users/index.html", context)

def login_view(request):
    # Show index page and message if a user has already logged in.
    if request.user.is_authenticated:
        context = {
            "loggedin": True
        }
        return render(request, "users/index.html", context)

    # Check entered information and log user in, or show error message.
    if request.method == "POST": 
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "users/login.html", {"message": "Invalid credentials."})
    
    # Show login page if user has not logged in.
    return render(request, "users/login.html")

def logout_view(request):
    # Log user out and return to the login page.
    logout(request)
    context = {
        "loggedin": False,
        "message": "Logged out."
    }
    return render(request, "users/login.html", context)

def register(request):
    # If a user registers, add the user to the database.
    if request.method == "POST": 
        first_name = request.POST["fname"]
        last_name = request.POST["lname"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password1"]
        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        # Create an order number for the current user.
        counter = Count.objects.first()
        set_order_number = Order(user=user, order_number=counter.counter)
        set_order_number.save()
        counter.counter=counter.counter+1
        counter.save()
        context = {
            "loggedin": False,
            "message": "You have succesfully registered."
        }
        return render(request, "users/login.html", context)
    
    # If a user dit not (yet) register, show the register form.
    return render(request, "users/register.html")

def menu(request):
    # Show the login page if a user is not logged in.
    if not request.user.is_authenticated:
        context = {
            "loggedin": False
        }
        return render(request, "users/login.html", context)

    # Get the order number for the current user.
    order_number = Order.objects.get(user=request.user, status='unpaid').order_number
    
    # Add selected toppings and additions to the order.
    if request.method == "POST": 
        if 'SelectTopping1' in request.POST.keys():
            topping = request.POST["SelectTopping1"]
            topping = Topping.objects.get(name=topping)
            add_item = OrderItem(user=request.user, order_number=order_number, item=topping, category="topping", price=topping.price) 
            add_item.save()
        if 'SelectTopping2' in request.POST.keys():
            topping = request.POST["SelectTopping2"]
            topping = Topping.objects.get(name=topping)
            add_item = OrderItem(user=request.user, order_number=order_number, item=topping, category="topping", price=topping.price) 
            add_item.save()
        if 'SelectTopping3' in request.POST.keys():
            topping = request.POST["SelectTopping2"]
            topping = Topping.objects.get(name=topping)
            add_item = OrderItem(user=request.user, order_number=order_number, item=topping, category="topping", price=topping.price) 
            add_item.save()
        if 'SelectAdditionCheese' in request.POST.keys():
            addition = request.POST["SelectAdditionCheese"]
            addition = Addition.objects.get(name=addition)
            add_item = OrderItem(user=request.user, order_number=order_number, item=addition, category="addition", price=addition.price)
            add_item.save()
        if 'SelectAddition1' in request.POST.keys():
            addition = request.POST["SelectAddition1"]
            addition = Addition.objects.get(name=addition)
            add_item = OrderItem(user=request.user, order_number=order_number, item=addition, category="addition", price=addition.price)
            add_item.save()
        if 'SelectAddition2' in request.POST.keys():
            addition = request.POST["SelectAddition2"]
            addition = Addition.objects.get(name=addition)
            add_item = OrderItem(user=request.user, order_number=order_number, item=addition, category="addition", price=addition.price)
            add_item.save()
        if 'SelectAddition3' in request.POST.keys():
            addition = request.POST["SelectAddition3"]
            addition = Addition.objects.get(name=addition)
            add_item = OrderItem(user=request.user, order_number=order_number, item=addition, category="addition", price=addition.price)
            add_item.save()
    
    # Get all the menu items from the database.
    context = {
        "regular_pizzas": RegularPizza.objects.all(),
        "sicilian_pizzas": SicilianPizza.objects.all(),
        "toppings": Topping.objects.all(),
        "subs": Sub.objects.all(),
        "pastas": Pasta.objects.all(),
        "salads": Salad.objects.all(),
        "dinnerplatters": Dinnerplatter.objects.all(),
        "loggedin": True
    }
    return render(request, "users/menu.html", context)

def add_to_order(request, category, name, price):
    # Show the login page if a user is not logged in.
    if not request.user.is_authenticated:
        context = {
            "loggedin": False
        }
        return render(request, "users/login.html", context)

    # Get the order number for this user and add the selected item to their shopping cart.
    order_number = Order.objects.get(user=request.user, status='unpaid').order_number
    add_item = OrderItem(user=request.user, order_number=order_number, item=name, category=category, price=price) 
    add_item.save()      
    return redirect(menu)

def shoppingcart(request):
    # Show the login page if a user is not logged in.
    if not request.user.is_authenticated:
        context = {
            "loggedin": False
        }
        return render(request, "users/login.html", context)
    
    # Get the order number for this user and check if they have at least one item in shopping cart.
    order_number = Order.objects.get(user=request.user, status='unpaid').order_number
    checkoneitem = False
    if len(OrderItem.objects.filter(user=request.user, order_number=order_number)) != 0:
        checkoneitem = True

    # Calculate the total order price.
    shoppingcart = OrderItem.objects.filter(user=request.user, order_number=order_number)
    totalprice = 0
    for item in shoppingcart:
        totalprice += item.price    

    # Show the shopping cart for the current user.
    context = {
        "shoppingcart": OrderItem.objects.filter(user=request.user, order_number=order_number),
        "checkoneitem": checkoneitem,
        "totalprice": totalprice,
        "loggedin": True
    }
    return render(request, "users/shoppingcart.html", context)

def place_order(request, price):
    # Show the login page if a user is not logged in.
    if not request.user.is_authenticated:
        context = {
            "loggedin": False
        }
        return render(request, "users/login.html", context)
    
    # Set the status of the placed order to 'paid'.
    user = request.user
    Order.objects.filter(user=user, status='unpaid').update(status='paid', price=price)
    
    # Create a new order number for this user.
    counter = Count.objects.first()
    set_order_number = Order(user=user, order_number=counter.counter, price=00.00)
    set_order_number.save()
    counter.counter=counter.counter+1
    counter.save()
    
    context = {
        "checkoneitem": False,
        "message": "Succes! We are now preparing your order.",
    }
    return render(request, "users/index.html", context)

def pick_toppings(request, category, name, price):
    # Show the login page if a user is not logged in.
    if not request.user.is_authenticated:
        context = {
            "loggedin": False
        }
        return render(request, "users/login.html", context)
    
    # Get the order number for this user and add the selected item to their shopping cart.
    order_number = Order.objects.get(user=request.user, status='unpaid').order_number
    add_item = OrderItem(user=request.user, order_number=order_number, item=name, category=category, price=price) 
    add_item.save()
    
    # Let user choose their toppings/additions.
    context = {
        "toppings": Topping.objects.all(),
        "item": name,
        "category": category,
        "additions": Addition.objects.all(),
        "loggedin": True
    }
    return render(request, "users/pick_toppings.html", context)

def addcoupon(request):
    # Get the order number for this user and get the items in their shopping cart.
    order_number = Order.objects.get(user=request.user, status='unpaid').order_number
    shoppingcart = OrderItem.objects.filter(user=request.user, order_number=order_number)
    
    # If the entered the coupon code, reduce their total order price.
    if request.method == "POST": 
        coupon = request.POST["coupon"]
        totalprice = 0
        for item in shoppingcart:
            totalprice += item.price
        if coupon == "freepizza":
            totalprice -= round(Decimal(12.70), 2)
        context = {
            "shoppingcart": OrderItem.objects.filter(user=request.user, order_number=order_number),
            "toppings": Topping.objects.all(),
            "checkoneitem": True,
            "totalprice": totalprice
        }
    return render(request, "users/shoppingcart.html", context)