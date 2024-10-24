from django.urls import path
from .views import addToCart, view_cart, updateCart

urlpatterns = [
    path('add-to-cart/<int:product_id>/', addToCart, name='AddToCart'),
    path('view-cart/', view_cart, name='ViewCart'),
    path('update-cart/<str:action>/<int:product_id>/', updateCart, name='UpdateCart')
]

