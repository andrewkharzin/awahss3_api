from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, custom_login
# from apps.profiles.views import ProfileDetailView, profile_detail

urlpatterns = [
    path('register', register, name='register'),
    path('login', custom_login, name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='auth/logout.html'), name='logout'),
    # path('profile/<agent_id>', profile_detail, name='profile-detail'),
    # path("followToggle/<str:author>/", followToggle, name="followToggle"),
    # path("followToggle/<str:author>/", followToggle, name="followToggle")

]