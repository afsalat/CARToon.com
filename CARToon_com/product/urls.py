from django.urls import path
from . import views


urlpetterns = [
    path('products/',views.veiwAllProducts, name="Home")
]