from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login, name="Login"),
    path('register/', views.Register, name="Register"),
    path('logout/', views.logout, name="Logout")
]