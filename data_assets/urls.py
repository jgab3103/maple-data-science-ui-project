from django.urls import path
from rest_framework import routers
from . import views_api
from django.conf.urls import url, include

app_name = "data_assets"

router = routers.DefaultRouter()
router.register('breaches', views_api.DataAssetBreachViewSet)
router.register('data-assets', views_api.DataAssetViewSet)
urlpatterns = [
    path("/v1/", include(router.urls)),
]
