from django.urls import path, include
from rest_framework import routers
from .views import *



urlpatterns = [
    # path('', include(router.urls))
    path('api/', include(('api.apps.users.routers', "core"), namespace='core-api')),
]