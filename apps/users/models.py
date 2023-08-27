from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from apps.users.managers import UserManager
from django.db.models.signals import post_save
from django.contrib.auth.models import Group
from django.dispatch import receiver


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), max_length=30, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)


    # following = models.ManyToManyField("self", blank=True, related_name="followers", symmetrical=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email
    
    class Roles(models.TextChoices):
        NOT_AUTHORIZED = 'new', _('New')
        AGENT = 'agent', _('Agent')
        ACCOUNT = 'account', _('Account')
        SHIFTLEADER = 'shiftleader', _('Shift Leader')
        MANAGER = 'manager', _('Manager')

    role = models.CharField(choices=Roles.choices, default=Roles.NOT_AUTHORIZED, max_length=20)


    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.email
    
    @property
    def is_new(self):
        return self.role == User.Roles.NOT_AUTHORIZED

    @property
    def is_agent(self):
        return self.role == User.Roles.AGENT

    @property
    def is_account(self):
        return self.role == User.Roles.ACCOUNT

    @property
    def is_shiftleader(self):
        return self.role == User.Roles.SHIFTLEADER

    @property
    def is_manager(self):
        return self.role == User.Roles.MANAGER



