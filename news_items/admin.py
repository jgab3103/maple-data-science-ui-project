from django.contrib import admin
from . import models

class NewsItemAdmin(admin.ModelAdmin):
    list_display = ('short_news_text',
                    'is_displayed',
                    'user')

admin.site.register(models.NewsItem, NewsItemAdmin)
