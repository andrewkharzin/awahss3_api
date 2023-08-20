from django.db import models
from apps.users.models import User
from phone_field import PhoneField
from birthday import BirthdayField, BirthdayManager
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _


def get_image_path(instance, filename):
    return 'user_profile_images/{0}/{1}'.format(instance.user.email, filename)



class Profile(models.Model):
    user = models.OneToOneField(
        User, related_name="profile", on_delete=models.CASCADE)
    first_name = models.CharField(
        _("First Name"), max_length=50, null=True, blank=True)
    second_name = models.CharField(
        _("Second Name"), max_length=50, null=True, blank=True)
    last_name = models.CharField(
        _("Last Name"), max_length=50, null=True, blank=True)
    position = models.CharField(
        "Position", max_length=50, null=True, blank=True)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    shift_work = models.BooleanField(_("Shift sched?"), default=0)
    birthday = BirthdayField(null=True)

    objects = BirthdayManager()

    image = models.ImageField(upload_to=get_image_path, null=True, blank=True)

    # def get_model_fields(agent):
    #     return agent._meta.get_field('agent_id')

    # def get_model_fields(organization):
    #     return organization._meta.get_fields('organization_name')

    @property
    def profile_preview(self):
        if self.image:
            return mark_safe('<img src="{}" width="80" />'.format(self.image.url))
        return ""

    def __str__(self):
        return self.user.get_username()

    @property
    def full_name(self):
        return "%s %s %s" % (self.first_name, self.last_name, self.second_name, )
