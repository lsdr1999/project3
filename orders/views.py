from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models import Sum
from .models import Category, Regular_pizza, Sicilian_pizza, Topping, Sub, Pasta, Salad, Dinner_platter, Order2, User_order, Order_counter

counter = Order_counter.objects.first()
if counter == None:
    set_counter = Order_counter(counter = 1)
    set_counter.save()
superuser = User.objects.filter(is_superuser = True)
if superuser.count() == 0:
    superuser = User.objects.create_user("admin", "admin@admin.com", "adminadmin")
    superuser.is_superuser = True
    superuser.is_staff = True
    superuser.save()
    set_superuser=User_order(user=superuser, order_number=counter.counter)
    set_superuser.save()


def index(request):
    if not request.user.is_authenticated:
        return render(request, "login.html", {"message":"Please log in or register."})
    context = {
        "user": request.user,
        "Categorys": Category.objects.all()
        }
    return render(request, "index.html", context)


def register(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if not request.POST["first_name"] or not request.POST["last_name"] or not request.POST["username"]:
            return render(request, "register.html", {"message":"You must provide a full name and username."})
        elif not request.POST["email"]:
            return render(request, "register.html", {"message":"You must provide an emailadress."})
        elif not request.POST["password"] or not request.POST["password2"]:
            return render(request, "register.html", {"message":"You must provide a password."})
        elif not password == password2:
            return render(request, "register.html", {"message":"Your password and confirmation should be the same."})

        if User.objects.filter(email=email).exists():
             return render(request, "register.html", {"message":"An account with this emailadress already exists, please log in."})

        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        counter = Order_counter.objects.first()
        order_number = User_order(user=user, order_number=counter.counter)
        order_number.save()
        counter.counter = counter.counter+1
        counter.save()
        return render(request, "login.html", {"message":"Registered. You can log in now."})
    else:
        return render(request, "register.html")


def login_view(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "login.html", {"message":"Please log in with the right username and password."})


def logout_view(request):
    logout(request)
    return render(request, "login.html", {"message": "Logged out."})


def menu(request):
    context = {
        "user": request.user,
        "Categorys": Category.objects.all(),
        "Regular_pizzas": Regular_pizza.objects.all(),
        "Sicilian_pizzas": Sicilian_pizza.objects.all(),
        "Toppings": Topping.objects.all(),
        "Subs": Sub.objects.all(),
        "Pastas": Pasta.objects.all(),
        "Salads": Salad.objects.all(),
        "Dinner_platters": Dinner_platter.objects.all(),
    }
    return render(request, "menu.html", context)


def order(request):
    order_number = User_order.objects.get(user=request.user, status='initiated').order_number
    context = {
        "user": request.user,
        "Checkout": Order2.objects.filter(user=request.user, number=order_number),
        "Total": list(Order2.objects.filter(user=request.user, number=order_number).aggregate(Sum('price')).values())[0],
        "Topping_price": 0.00,
        "Order_number": order_number
    }
    return render(request, "order.html", context)


def add(request, category, name, price):
    order_number = User_order.objects.get(user=request.user, status='initiated').order_number
    topping_allowance = User_order.objects.get(user=request.user, status='initiated')
    context = {
        "user": request.user,
        "Checkout": Order2.objects.filter(user=request.user, number=order_number),
        "Total": list(Order2.objects.filter(user=request.user, number=order_number).aggregate(Sum('price')).values())[0],
        "Topping_price": 0.00,
        "Order_number": order_number
    }

    if 'Regular Pizza' or 'Sicilian Pizza':
        if name == "1 topping":
            topping_allowance.topping_allowance+=1
            topping_allowance.save()
        if name == "2 toppings":
            topping_allowance.topping_allowance+=2
            topping_allowance.save()
        if name == "3 toppings":
            topping_allowance.topping_allowance+=3
            topping_allowance.save()
    if "Toppings" and topping_allowance.topping_allowance == 0:
        return render(request, "order.html", context)
    if "Toppings" and topping_allowance.topping_allowance > 0:
        topping_allowance.topping_allowance-=1
        topping_allowance.save()

    add = Order2(user=request.user, number=order_number, category=category, name=name, price=price)
    add.save()
    context2 = {
        "user": request.user,
        "Checkout": Order2.objects.filter(user=request.user, number=order_number),
        "Total": list(Order2.objects.filter(user=request.user, number=order_number).aggregate(Sum('price')).values())[0],
        "Topping_price": 0.00,
        "Order_number": order_number
    }
    return render(request, "order.html", context2)

# def delete(request,category,name,price):
#     order_number = User_order.objects.get(user=request.user, status='initiated').order_number
#     topping_allowance = User_order.objects.get(user=request.user, status='initiated')
#     if 'Regular Pizza' or 'Sicilian Pizza':
#         if name == "1 topping":
#             topping_allowance.topping_allowance+=1
#             topping_allowance.save()
#         if name == "2 toppings":
#             topping_allowance.topping_allowance+=2
#             topping_allowance.save()
#         if name == "3 toppings":
#             topping_allowance.topping_allowance+=3
#             topping_allowance.save()
#         topping_allowance.topping_allowance = 0
#         topping_allowance.save()
#         delete_all_toppings = Order2.objects.filter(user=request.user,category="Toppings")
#         delete_all_toppings.delete()
#     if "Toppings":
#         topping_allowance.topping_allowance+=1
#         topping_allowance.save()
#
#     find_order = Order2.objects.filter(user=request.user, category=category, name=name, price=price)[0]
#     find_order.delete()
#     context = {
#         "user": request.user,
#         "Checkout": Order2.objects.filter(user=request.user, number=order_number),
#         "Total": list(Order2.objects.filter(user=request.user, number=order_number).aggregate(Sum('price')).values())[0],
#         "Topping_price": 0.00,
#         "Order_number": order_number
#     }
#     return render(request,"order.html",context)
