from django.urls import path
from .views import index


urlpatterns = [
    path("company/", index, name="index"),
]