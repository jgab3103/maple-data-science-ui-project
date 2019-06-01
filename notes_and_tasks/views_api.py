from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from . import models


class NoteOrTaskViewSet(viewsets.ModelViewSet):
    queryset = models.NoteOrTask.objects.all()
    serializer_class = serializers.NoteOrTaskSerializer
