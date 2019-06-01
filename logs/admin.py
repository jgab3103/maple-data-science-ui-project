from django.contrib import admin
from . import models



class DataUploadLogAdmin(admin.ModelAdmin):
    list_display = ('date',
                    'message',
                    'status',
                    )

admin.site.register(models.DataUploadLog, DataUploadLogAdmin)
# Register your models here.
