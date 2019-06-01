from django.contrib import admin
from django.urls import include, path
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls import url
from markdownx import urls as markdownx

schema_view = get_swagger_view(title='CIDA Data API')

admin.site.site_header = 'Maple Administration'

urlpatterns = [
    url(r'^markdownx/', include('markdownx.urls')),
    path('swagger/', schema_view),
    path('admin/', admin.site.urls),
    path('maple/', include('main.urls')),
    path('news-items-api', include('news_items.urls')),
    path('research-projects-api', include('data_projects.urls')),
    path('data-assets-api', include('data_assets.urls')),
    path('requests-api', include('projects.urls')),
    path('accounts-api', include('accounts.urls')),
    path('notes-and-tasks-api', include('notes_and_tasks.urls')),
    path('apps-and-notebooks-api', include('apps_and_notebooks.urls')),
    path('accounts/', include('django.contrib.auth.urls')),


]
