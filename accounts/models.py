from django.contrib.auth.models import User
from django.db import models

# Extend django user profile as per:
# https://docs.djangoproject.com/en/2.2/topics/auth/customizing/

class ExtendedProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=100, blank=True)
    orcid = models.CharField(max_length = 100, blank=True)
    researchgate_id = models.CharField(max_length = 255, blank = True)
