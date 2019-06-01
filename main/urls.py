from django.urls import path
from django.conf.urls import url, include


from . import views
from . import views_reports

app_name = "main"

urlpatterns = [
    path('', views.index, name = 'index'),
    path('data-api', views.data_api, name = "data_api"),
    path('metadata', views.metadata, name = "metadata"),
    path('news/<int:news_item_id>/', views.news_item, name='news_item'),
    path('task-note-edit/<int:id>', views.edit_task_or_note, name = "task_note_edit"),
    path('metadata/<int:asset_id>/', views.metadata_detail, name = "metadata_detail"),
    path('data-onboarding', views.dataonboarding, name = "data_onboarding"),
    path('resources', views.resources, name = "resources"),
    path('data-requests', views.data_requests, name = "data_requests"),
    path('data-projects', views.data_projects, name='data_projects'),
    path('data-project-review', views.data_project_review, name='data_project_review'),
    path('apps-and-notebooks', views.apps_and_notebooks, name='apps_and_notebooks'),
    path('data-projects/<int:data_project_id>/', views.data_projects_detail, name = "projects_detail"),
    path('data-project-review-detail/<int:data_project_id>/', views.data_projects_review_detail, name = "projects_review"),
    path('forms', views.forms, name = "forms"),
    path('submit-data-request', views.submit_data_request, name = "submit_data_request"),
    url(r'^data-requests/(?P<var1>\d+)/$', views.DataRequestDetailView.as_view(), name = "main"),
    url(r'^data-project-output/(?P<var1>\d+)/$', views.DataProjectOutputDetailView.as_view(), name = "main"),
    path('question/submit', views.NoteFormView.as_view(), name='question'),
    path('data-project-output-note', views.DataProjectOutputNoteFormView.as_view(), name='dpo_submit'),
    path('answer/submit', views.TaskFormView.as_view(), name='answer'),
    path('status/change', views.UpdateStatusFormView.as_view(), name='status_change'),
    path("thanks",views.thanks),
    path('profile', views.user_profile),
    path("assets-report", views_reports.assets_report),
    path("users-report", views_reports.users_report),


]
