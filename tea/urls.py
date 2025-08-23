from django.contrib import admin
from django.urls import path, include
from . import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tweet.urls')),   # ✅ include your app urls
    path('', views.index),   # ✅ include your app urls
]
