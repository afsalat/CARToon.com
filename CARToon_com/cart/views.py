from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart
from product.models import Product
from user.models import customUser
from django.contrib.auth.decorators import login_required

# Endpoint: Add a product to the cart
@login_required  # Ensure the user is logged in
def addToCart(request, product_id):
    try:
        product = get_object_or_404(Product, id=product_id)  
        user = request.user  # Get the currently logged-in user

        # Use the user instance directly
        cart_item, created = Cart.objects.get_or_create(
            pro_id=product,
            user_id=user,
            defaults={'quantity': 1}
        )

        if not created:
            cart_item.quantity += 1 
            cart_item.save()  # Save the updated quantity if not created

        return redirect('ViewCart')  # Redirect to the cart view
    except Exception as e:
        print(e)  # Log the error for debugging
        return render(request, 'Home.html', {'message': str(e)})

# Endpoint: View all items in the cart
@login_required  # Ensure the user is logged in
def view_cart(request):
    try:
        user = request.user  # Get the currently logged-in user
        cart_items = Cart.objects.filter(user_id=user)  # Fetch cart items for the user
        return render(request, 'Cart.html', {"cart_items": cart_items})
    except Exception as e:
        return render(request, 'Home.html', {'message': str(e)})

# Endpoint: Update the quantity of items in the cart
@login_required  # Ensure the user is logged in
def updateCart(request, action, product_id):
    try:
        user = request.user  # Get the currently logged-in user
        cart_item = get_object_or_404(Cart, pro_id__id=product_id, user_id=user)

        if action == 'add':
            cart_item.quantity += 1
        elif action == 'remove':
            cart_item.quantity -= 1

        if cart_item.quantity <= 0:
            cart_item.delete()  # Remove the item if quantity is 0
        else:
            cart_item.save()  # Save the updated quantity

        return redirect('ViewCart')  # Redirect to the cart view
    except Exception as e:
        return render(request, 'Home.html', {'message': str(e)})
