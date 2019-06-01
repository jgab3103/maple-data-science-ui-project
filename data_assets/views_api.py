from django.shortcuts import render
from django.http import HttpResponseRedirect
from rest_framework import viewsets
from . import serializers
from . import models

class DataAssetBreachViewSet(viewsets.ModelViewSet):
    queryset = models.DataAssetBreach.objects.all()
    serializer_class = serializers.DataAssetBreachSerializer


class DataAssetViewSet(viewsets.ModelViewSet):
    queryset = models.DataAsset.objects.all()
    serializer_class = serializers.DataAssetSerializer
