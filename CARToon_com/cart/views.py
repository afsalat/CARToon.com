import traceback
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart
from product.models import Product



# Endpoint: Add a product to the cart
def addToCart(request, product_id):
    try:
        product = get_object_or_404(Product, id=product_id)  
        user = request.user
        print(user.id)

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

        product_ids = cart_items.values_list('pro_id', flat=True)  
        products = Product.objects.filter(id__in=product_ids)  

        cart_items_with_products = [
            {'cart_item': item, 'product': products.get(id=item.pro_id)} for item in cart_items
        ]

        total_amount = sum(item['product'].pro_price * item['cart_item'].quantity for item in cart_items_with_products)

        return render(request, 'Cart.html', {"cart_items_with_products": cart_items_with_products, "total_amount": total_amount})


    except Exception as e:
        print(f"Error while viewing cart: {e}") 
        print(traceback.format_exc())
        return render(request, 'Home.html', {'message': 'An error occurred while fetching your cart.'})




# Endpoint: Update the quantity of items in the cart
def updateCart(request, action, product_id):
    try:
        user = request.user  
        cart_item = get_object_or_404(Cart, pro_id=product_id, user_id=user.id)

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
