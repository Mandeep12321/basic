from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from django.utils import timezone
from .manager import CustomUserManager
from multiselectfield import MultiSelectField
# Create your models here.
class User(AbstractBaseUser,PermissionsMixin):
    first_name = models.CharField(_('first_name'),max_length=255)
    last_name = models.CharField(_('last_name'),max_length=255)
    email = models.EmailField(_('email'),unique=True)
    gender = models.CharField(max_length=25,default="",blank=True)
    Hobbies = MultiSelectField(max_length=100)
    img = models.ImageField(upload_to='profilepic/', null=True, blank=True)
    country = models.CharField(max_length=255,default="",blank=True)

    is_staff = models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.')
    is_active = models.BooleanField(default=True,
                                    help_text='Designates whether this user should be treated as active.\
                                                 Unselect this instead of deleting accounts.')
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    USERNAME_FIELD = 'email'
    objects = CustomUserManager()

    def __str__(self):
        return self.email