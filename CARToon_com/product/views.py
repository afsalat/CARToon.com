from urllib import response
from django.shortcuts import render
from .models import Product


#Endpoint: view all products
def veiwAllProducts(request):
    try:
        products = Product.objects.all()
        render(request, "Home.html", {"products":products})
    except Exception as e:
        return response({'message':str(e), 'status_code':500})