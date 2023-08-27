from django.urls import path
from . import views

urlpatterns = [
    # ...
    path('admin/check-parse/', views.check_parse, name='check-parse'),
    # ...
]