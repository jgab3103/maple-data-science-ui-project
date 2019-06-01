from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from . import models

class RequestViewSet(viewsets.ModelViewSet):
    queryset = models.DataRequest.objects.all()
    serializer_class = serializers.RequestSerializer
