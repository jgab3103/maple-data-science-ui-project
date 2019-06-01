from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from . import models

# Extend django user profile as per:
# https://docs.djangoproject.com/en/2.2/topics/auth/customizing/

class ExtendedProfileInline(admin.StackedInline):
    model = models.ExtendedProfile
    can_delete = False
    verbose_name_plural = 'Extended profile'

class UserAdmin(BaseUserAdmin):
    inlines = (ExtendedProfileInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
