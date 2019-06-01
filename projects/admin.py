from django.contrib import admin
from . import models




class DataRequestAdmin(admin.ModelAdmin):
    list_filter = ['current_status', 'date_received', 'data_type']
    list_display = ('date_received',
                    'data_type',
                    'detail',
                    'related_documentation',
                    'current_status',
                    'currently_assigned_to',
                    'requestor_contact_name',
                    )




admin.site.register(models.DataRequest, DataRequestAdmin)
