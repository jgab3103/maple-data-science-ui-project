from django.contrib import admin
from . import models
# Register your models here.


class ChangeLogInline(admin.TabularInline):
    model = models.ChangeLog
    extra = 0


class DataAPIAdmin(admin.ModelAdmin):
    list_display = (
            'title',
            'version',
            'type',
            'formats_supported'
    )
    inlines = [ChangeLogInline,]

admin.site.register(models.DataAPI, DataAPIAdmin)
