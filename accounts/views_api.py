from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from django.contrib.auth.models import User
from . import models

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
