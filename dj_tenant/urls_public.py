from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin-tenant/', admin.site.urls),
    path('', include('clients.urls')),
    
]