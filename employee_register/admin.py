from django.contrib import admin
from .models import User


class AdminUser(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','img','password']

# Register your models here.
admin.site.register(User,AdminUser)