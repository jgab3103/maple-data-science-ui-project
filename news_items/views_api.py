from django.shortcuts import render
from django.http import HttpResponseRedirect
from rest_framework import viewsets
from . import serializers
from . import models

class NewsItemViewSet(viewsets.ModelViewSet):
    queryset = models.NewsItem.objects.all()
    serializer_class = serializers.NewsItemSerializer
