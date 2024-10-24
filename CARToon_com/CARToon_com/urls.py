from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(), name='login'),  
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
    path('register/', include('user.urls')),  
    path('', include('user.urls')),
    path('', include('cart.urls')),
    path('', include('product.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
