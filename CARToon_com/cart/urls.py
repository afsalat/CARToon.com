from django.urls import path
from . import views


urlpatterns = [
    path('add-to-cart/<int:product_id>/', views.addToCart, name="AddToCart"),
    path('view-all-items/<int:user_id>/', views.view_cart, name="ViewCart"),
    path('update-cart/<str:action>/<int:product_id>/', views.upadateCart, name="UpdateCart")
]