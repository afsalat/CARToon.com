from django.shortcuts import render
from .models import Product


# Endpoint: view all products
def viewAllProducts(request):
    try:
        products = Product.objects.all()
        print("----", products)
        data=[item for item in products]
        return render(request, 'Home.html', {'products': data})

    except Exception as e:
        return render(request, 'Home.html', {'message': str(e), 'status_code': 500})
