from django.urls import path
from .views import MsgShcClassesList

urlpatterns = [
    path('msg-shc/', MsgShcClassesList.as_view(), name='msg-shc-list'),
]