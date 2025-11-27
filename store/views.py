from django.shortcuts import render

# Create your views here.

from .models import Category, Product

def categories(request):
    categories= Category.objects.all()
    return categories

def all_products(request):
    products= Product.objects.all()
    return render(request, "store/home.html", {'products':Product})
