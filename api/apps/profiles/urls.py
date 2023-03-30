from django.urls import path, include
from rest_framework import routers
from .views import *


# router = routers.DefaultRouter()
# router.register(r'profiles', ProfileViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('', include(router.urls)),
    path('follow_unfollow/', FollowUnfollowView.as_view(), name = "follow_unfollow"),
]

# urlpatterns += router.urls