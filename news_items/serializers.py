from rest_framework import serializers
from . import models


class NewsItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NewsItem
        fields = (
         'date_added',
         'news_text',
         'is_displayed',
         'user'
        )
