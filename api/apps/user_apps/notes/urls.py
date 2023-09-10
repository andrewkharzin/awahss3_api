from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'notes', views.NoteViewSet)
router.register(r'categories', views.CategoryViewSet)

urlpatterns = [
    # Other API endpoints if needed
    path('notes/', include(router.urls)),
]
