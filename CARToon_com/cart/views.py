import traceback
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart
from product.models import Product
from user.models import customUser
from django.contrib.auth.decorators import login_required



# Endpoint: Add a product to the cart
def addToCart(request, product_id):
    try:
        product = get_object_or_404(Product, id=product_id)  
        user = request.user
        print(user)

        cart_item, created = Cart.objects.get_or_create(
            pro_id=product.id,
            user_id=user.id,
            defaults={'quantity': 1}
        )

        if not created:
            cart_item.quantity += 1 
            cart_item.save() 

        return redirect('ViewCart')  
    except Exception as e:
        print(e)  
        return render(request, 'Home.html', {'message': str(e)})


# Endpoint: View all items in the cart
def view_cart(request):
    try:
        user = request.user 
        cart_items = Cart.objects.filter(user_id=user.id)

        if not cart_items.exists():  
            return render(request, 'Cart.html', {"cart_items": cart_items, "message": "Your cart is empty."})

        products = []
        for item in cart_items:
            product = Product.objects.get(id=item.pro_id)
            products.append(product)

        return render(request, 'Cart.html', {"cart_items": cart_items, "products": products})

    except Exception as e:
        print(f"Error while viewing cart: {e}") 
        print(traceback.format_exc())
        return render(request, 'Home.html', {'message': 'An error occurred while fetching your cart.'})



# Endpoint: Update the quantity of items in the cart
def updateCart(request, action, product_id):
    try:
        user = request.user  
        cart_item = get_object_or_404(Cart, pro_id__id=product_id, user_id=user.id)

        if action == 'add':
            cart_item.quantity += 1
        elif action == 'remove':
            cart_item.quantity -= 1

        if cart_item.quantity <= 0:
            cart_item.delete() 
        else:
            cart_item.save()  

        return redirect('ViewCart')  
    except Exception as e:
        return render(request, 'Home.html', {'message': str(e)})
