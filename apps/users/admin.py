from django.contrib import admin
from apps.users.profile.profile import Profile
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from apps.users.models import User



admin.site.register(User)



# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):   
    model = Profile

    list_display = ('id', 'user', 'user_id', 'full_name', 'phone', 'birthday', 'shift_work', 'profile_preview')
    readonly_fields = ('profile_preview',)

    raw_id_fields = ['user', ]

    def profile_preview(self, obj):
        return obj.profile_preview

    profile_preview.short_description = 'Profile Preview'
    profile_preview.allow_tags = True