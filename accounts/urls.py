from django.urls import path
from rest_framework import routers
from . import views_api
from django.conf.urls import url, include

app_name = "accounts"

router = routers.DefaultRouter()
router.register('users', views_api.UserViewSet)

urlpatterns = [
    path("/v1/", include(router.urls)),
]
