from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todoApp.urls')),  # So we can see the urls from the todoApp
]
