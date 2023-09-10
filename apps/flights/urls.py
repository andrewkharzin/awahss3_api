from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    # ...
    path('admin/check-parse/', views.check_parse, name='check-parse'),
    # Other URL patterns
  
]
