from django.contrib import admin
from . import models
# Register your models here.

class DataProjectOutputInline(admin.StackedInline):
    model = models.DataProjectOutput
    extra = 0

class DataProjectInvestigatorInline(admin.TabularInline):
    model = models.DataProjectInvestigator
    extra = 0


class DataProjectOutputInvestigatorInline(admin.TabularInline):
    model = models.DataProjectOutputInvestigator
    extra = 0


class RequiredApprovalInline(admin.StackedInline):
    model = models.RequiredApproval
    extra = 0


class DataProjectGrantApplicationReviewInline(admin.TabularInline):
     model = models.DataProjectGrantApplicationReview
     extra = 0


class DataProjectGrantApplicationReviewerScoreInline(admin.StackedInline):
    model = models.DataProjectGrantApplicationReviewerScore
    extra = 0



class DataProjectOutputAdmin(admin.ModelAdmin):
    list_display = (
            'output_title',
            'start_date',
            'expected_release_date',
            'actual_release_date',
            'data_project',
            'output_type'
    )
    inlines = [DataProjectOutputInvestigatorInline, RequiredApprovalInline]

#
class DataProjectGrantApplicationReviewAdmin(admin.ModelAdmin):
    list_display = (
    'grant_id',
    'application_title',
    'ci_prefix',
    'ci_name',
        'status_of_review',
    )

    inlines = [DataProjectGrantApplicationReviewerScoreInline,]


class DataProjectAdmin(admin.ModelAdmin):
    list_display = (
     'title',
     'summary',
     'research_type',
     'related_documentation_location',
     'internal_investigators_only',
    )

    inlines = [RequiredApprovalInline, DataProjectInvestigatorInline, DataProjectOutputInline, ]

class DataProjectGrantApplicationReviewerScoreAdmin(admin.ModelAdmin):
    list_display = (
     'reviewer_name',
     'application',
     'significance_score',
     'team_track_record_score',
     'translation_score',
     'sustainability_score',
    )


class DataProjectInvestigatorAdmin(admin.ModelAdmin):
    list_display = (
     'investigator_name',
     'data_project',
     'role',
    )

class DataProjectOutputInvestigatorAdmin(admin.ModelAdmin):
    list_display = (
     'investigator_name',
     'project_output',
    )


class RequiredApprovalAdmin(admin.ModelAdmin):
    list_display = (
     'approval_from',
     'approval_contact_name',
     'approval_end_date',
     'granted'
    )

admin.site.register(models.RequiredApproval, RequiredApprovalAdmin)
admin.site.register(models.DataProjectOutput, DataProjectOutputAdmin)
admin.site.register(models.DataProject, DataProjectAdmin)
admin.site.register(models.DataProjectInvestigator, DataProjectInvestigatorAdmin)
admin.site.register(models.DataProjectOutputInvestigator, DataProjectOutputInvestigatorAdmin)
admin.site.register(models.DataProjectGrantApplicationReview, DataProjectGrantApplicationReviewAdmin)
admin.site.register(models.DataProjectGrantApplicationReviewerScore, DataProjectGrantApplicationReviewerScoreAdmin)
