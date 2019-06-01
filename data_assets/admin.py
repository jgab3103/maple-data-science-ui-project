from django.contrib import admin
from . import models

class DataAssetRoleInline(admin.TabularInline):
    model = models.DataAssetRole
    extra = 0

class DataBreachAdmin(admin.ModelAdmin):
    list_display = (
    'date_of_report',
    'summary',
    'related_documentation')

class DataAssetAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'owning_business_unit',
                    'start_date',
                    'end_date',
                    )
    list_filter = ['owning_business_unit', 'type']
    search_fields = ('name',)
    inlines = [DataAssetRoleInline, ]



class DataAssetRoleAdmin(admin.ModelAdmin):

    list_display = ('user',
                    'type',
                    'data_asset',
                    'start_date',
                    'end_date',
                    )


class DataElementAdmin(admin.ModelAdmin):
    list_filter = ['category', 'type', 'name_is_conformed', 'under_review']
    search_fields = ('name',)
    list_display = (
    "element_id",
    "name",
    "name_is_conformed",
    "type",
    "category",
    "under_review"
    )

admin.site.register(models.DataAsset, DataAssetAdmin)
admin.site.register(models.DataAssetBreach, DataBreachAdmin)
admin.site.register(models.DataElementAcceptedValue)
admin.site.register(models.DataElement, DataElementAdmin)
admin.site.register(models.DataAssetRole, DataAssetRoleAdmin)
