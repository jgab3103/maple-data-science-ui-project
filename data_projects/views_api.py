from django.shortcuts import render
from django.http import HttpResponseRedirect
from rest_framework import viewsets
from . import serializers
from . import models

class ResearchProjectViewSet(viewsets.ModelViewSet):
    queryset = models.DataProject.objects.all()
    serializer_class = serializers.ResearchProjectSerializer

class ResearchProjectOutputViewSet(viewsets.ModelViewSet):
    queryset = models.DataProjectOutput.objects.all()
    serializer_class = serializers.ResearchProjectOutputSerializer

class ResearchProjectGrantApplicationReviewViewSet(viewsets.ModelViewSet):
    queryset = models.DataProjectGrantApplicationReview.objects.all()
    serializer_class = serializers.ResearchProjectGrantApplicationReviewSerializer

class ResearchProjectGrantApplicationReviewerScoreViewSet(viewsets.ModelViewSet):
    queryset = models.DataProjectGrantApplicationReviewerScore.objects.all()
    serializer_class = serializers.ResearchProjectGrantApplicationReviewerScoreSerializer
