from django.urls import path
from django.conf.urls import url, include


from . import views

app_name = "data_api"

urlpatterns = [
    path('', views.index, name = 'index'),

]
