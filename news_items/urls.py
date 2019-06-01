from django.urls import path
from rest_framework import routers
from . import views_api
from django.conf.urls import url, include

app_name = "news_items"

router = routers.DefaultRouter()
router.register('news_items', views_api.NewsItemViewSet)
urlpatterns = [
    path("/v1/", include(router.urls)),
]
