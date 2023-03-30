from django.urls import path, include

from rest_framework import routers


from .views import *

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
#     TokenVerifyView,
# )

# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'profiles', ProfileViewSet)
# # router.register(r'profiles', ProfileViewSet)
# # router.register(r'projects', ProjectViewSet)

# # router.register(r'notes', NoteViewSet)
# router.register('ping', PingViewSet, basename="ping")


urlpatterns = [
    # path('airlines', include('api.apps.directory.airlines.url'))

    # path('profiles', include("api.apps.profiles.urls")),
    
    # path('', include(router.urls)),
    # path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('register/', RegisterView.as_view(), name="sign_up"),
    # path('verify_token/', TokenVerifyView.as_view(), name='token_verify')
]