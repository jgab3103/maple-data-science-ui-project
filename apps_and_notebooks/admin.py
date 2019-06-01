from django.contrib import admin
from . import models

class AppOrNotebookAdmin(admin.ModelAdmin):
    list_display = ('created_by',
                    'title',
                    'release_date'
                    )

admin.site.register(models.AppOrNotebook, AppOrNotebookAdmin)
