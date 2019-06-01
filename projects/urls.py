from django.urls import path
from rest_framework import routers
from . import views_api
from django.conf.urls import url, include

app_name = "projects"

router_v1 = routers.DefaultRouter()
router_v1.register('requests', views_api.RequestViewSet)

# router_v2 = routers.DefaultRouter()
# router_v2.register('requests', views_api.RequestViewSet)

urlpatterns = [
    path("/v1/", include(router_v1.urls)),
    # path("/v2/", include(router_v2.urls)),
]
