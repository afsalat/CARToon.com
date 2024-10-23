from urllib import response
from django.shortcuts import get_object_or_404, render
from .models import Cart
from product.models import Product


#Endpoint: add to cart
def addToCart(request, product_id):
    try:
        cart = Cart.objects.get_or_create(user_id=request.user, product_id=product_id)
        product = Product.objects.filter([item for item in cart]).all()
        
        if not cart:
            cart.quantity += 1
            cart.save()

        return render(request, 'Cart.html', {'cart': cart, 'product':product})
    except Exception as e:
        return response({'meesage':str(e), 'status_code':500})
    

#Endpoint: update cart
def upadateCart(request):
    try:
        if request.method == "POST":
            pass
    except Exception as e:
        return response({'meesage':str(e), 'status_code':500})
    

#Endpoint: view all cart items
def view_cart(request):
    try:
        cart = Cart.objects.get(user=request.user)
        product = Product.objects.filter([item for item in cart])

        return render(request, 'cart.html', {'cart': cart, 'product': product})
    except Exception as e:
        return response({'meesage':str(e), 'status_code':500})