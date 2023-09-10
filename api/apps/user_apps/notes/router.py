from rest_framework import routers
from .views import NoteViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r'notes', NoteViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    # Your existing URL patterns go here
]

urlpatterns += router.urls
