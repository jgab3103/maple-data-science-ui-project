from django.urls import path
from rest_framework import routers
from . import views
from django.conf.urls import url, include

app_name = "apps_or_notebooks"

router = routers.DefaultRouter()
router.register('apps-and-notebooks', views.AppOrNotebookViewSet)

urlpatterns = [
    path("/v1/", include(router.urls)),
]
