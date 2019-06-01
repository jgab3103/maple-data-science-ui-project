from django.contrib import admin

from . import models



class NoteOrTaskAdmin(admin.ModelAdmin):
    list_display = ('allocated_to',
                    'detail',
                    'date_due',
                    )





admin.site.register(models.NoteOrTask, NoteOrTaskAdmin)
