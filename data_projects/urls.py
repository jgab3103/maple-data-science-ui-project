from django.urls import path
from rest_framework import routers
from . import views_api
from django.conf.urls import url, include

app_name = "data_projects"

router = routers.DefaultRouter()
router.register('research_projects', views_api.ResearchProjectViewSet)
router.register('research_project_ouputs', views_api.ResearchProjectOutputViewSet)
router.register('research_project_grant_application_reviews', views_api.ResearchProjectGrantApplicationReviewViewSet)
router.register('research_project_grant_application_reviewer_scores', views_api.ResearchProjectGrantApplicationReviewerScoreViewSet)

urlpatterns = [
    path("/v1/", include(router.urls)),
]
