from django.shortcuts import render, redirect
from .models import Product
from django.conf import settings

from django.http import HttpResponseForbidden


# Create your views here.
def home_view(request):
    data = Product.objects.all()

    return render(request, "home.html", {'data': data})

def dashboard_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        image = request.POST.get('image')

        product = Product(name=name, price=price, description=description, image=image)
        product.save()
        redirect('dashboard')
    return render(request, "dashboard.html")


def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")




