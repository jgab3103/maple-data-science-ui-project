from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count
from markdownx.models import MarkdownxField
from data_assets.models import DataAsset

APPLICATION_STATUS_CHOICES = (
    ("Under review", "Under review"),
    ("Reviewed", "Reviewed")
)

DATA_PROJECT_OUTPUT_TYPE_CHOICES = (
    ("Government report", "Government report"),
    ("Conference paper", "Conference paper"),
    ("Journal article", "Journal article"),
    ("App or notebook", "App or notebook")
)

DATA_PROJECT_INVESTIGATOR_CHOICES = (
    ("Lead investigator", "Lead investigator"),
    ("Investigator", "Investigator"),
    ("Co-investigator", "Co-investigator")
)


DATA_PROJECT_RESEARCH_TYPE_CHOICES = (
    ("Quality improvement only", "Quality improvement only"),
    ("Journal publication and quality improvement", "Journal publication and quality improvement"),
)


DATA_PROJECT_CURRENT_STATUS_CHOICES = (
    ("Active", "Active"),
    ("Not yet active", "Not yet active"),
    ("On hold", "On hold"),
)

DATA_PROJECT_OUTPUT_CURRENT_STATUS_CHOICES = (
    ("Scoping and preliminary analysis", "Scoping and preliminary analysis"),
    ("Awaiting approval to commence draft", "Awaiting approval to commence draft"),
    ("Preparing draft", "Preparing draft"),
    ("Awaiting internal approval for draft", "Awaiting internal approval for draft"),
    ("Submitted to journal or conference", "Submitted to journal or conference"),
    ("Accepted", "Accepted"),
    ("Completed", "Completed"),
)




class DataProject(models.Model):
    title = models.CharField(max_length = 255)
    summary = MarkdownxField()
    research_type = models.CharField(max_length = 200, choices = DATA_PROJECT_RESEARCH_TYPE_CHOICES)
    related_documentation_location = models.CharField(max_length = 100)
    working_folder = models.CharField(max_length = 200)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    internal_investigators_only = models.BooleanField(default = True)
    current_status = models.CharField(max_length = 100, choices = DATA_PROJECT_CURRENT_STATUS_CHOICES)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.title



class DataProjectInvestigator(models.Model):
    investigator_name = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    data_project = models.ForeignKey(DataProject, on_delete=models.CASCADE, null=True)
    role = models.CharField(max_length = 255, choices = DATA_PROJECT_INVESTIGATOR_CHOICES)

    def __str__(self):
        return self.investigator_name.username

class DataProjectOutput(models.Model):
    data_project = models.ForeignKey(DataProject, on_delete=models.CASCADE, null=True)
    output_title = models.CharField(max_length = 255)
    publication_or_conference_name = models.CharField(max_length = 255, null = True)
    related_documentation = models.CharField(max_length = 100)
    summary = MarkdownxField()
    working_folder = models.CharField(max_length = 200)
    start_date = models.DateField(null=True, blank=True)
    expected_release_date = models.DateField(null=True, blank=True)
    actual_release_date = models.DateField(null=True, blank=True)
    output_type = models.CharField(max_length = 200, choices = DATA_PROJECT_OUTPUT_TYPE_CHOICES)
    current_status = models.CharField(max_length = 100, choices = DATA_PROJECT_OUTPUT_CURRENT_STATUS_CHOICES)
    pubmed_id = models.CharField(max_length = 50, blank=True, null=True)
    data_assets = models.ManyToManyField(DataAsset, blank=True)

    def __str__(self):
        return self.output_title


class RequiredApproval(models.Model):
    approval_from = models.CharField(max_length = 100)
    approval_contact_name = models.CharField(max_length = 255)
    approval_start_date = models.DateField(null = True, blank = True)
    approval_end_date = models.DateField(null = True, blank = True)
    approval_reference = models.CharField(max_length = 100)
    data_project_output = models.ForeignKey(DataProjectOutput, on_delete=models.CASCADE, null=True, blank=True)
    data_project = models.ForeignKey(DataProject, on_delete=models.CASCADE, null=True, blank=True)
    granted = models.BooleanField(default = False)

    def __str__(self):
        return self.approval_from


class DataProjectOutputInvestigator(models.Model):
    investigator_name = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    project_output = models.ForeignKey(DataProjectOutput, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.investigator_name.username


class DataProjectGrantApplicationReview(models.Model):
    grant_id = models.CharField(max_length = 100)
    ci_prefix = models.CharField(max_length = 255)
    ci_name = models.CharField(max_length = 255)
    application_title = models.CharField(max_length = 255)
    administering_organisation = models.CharField(max_length = 255)
    lead_organisation = models.CharField(max_length = 255)
    status_of_review = models.CharField(max_length = 100, choices = APPLICATION_STATUS_CHOICES)

    def __str__(self):
        return self.grant_id


class DataProjectGrantApplicationReviewerScore(models.Model):
    reviewer_name = models.CharField(max_length = 255)
    application = models.ForeignKey(DataProjectGrantApplicationReview, on_delete=models.CASCADE, null=True)
    significance_score = models.FloatField()
    team_track_record_score = models.FloatField()
    translation_score =  models.FloatField()
    sustainability_score =  models.FloatField()
    comments = models.TextField()
    date_finalised = models.DateField(auto_now_add = True, blank=True, null=True)

    def __str__(self):
        return self.reviewer_name
