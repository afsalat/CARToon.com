from django.urls import path, include
from . import views


urlpatterns = [
    path('products/',views.viewAllProducts, name="home"),
]