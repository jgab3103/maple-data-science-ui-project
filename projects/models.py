from django.db import models
from datetime import datetime
from data_assets.models import DataAsset
from django.contrib.auth.models import User

STATUS_CHOICES = (
        ('Awaiting triage', 'Awaiting triage'),
        ('Being processed', 'Being processed'),
        ('Approved', 'Approved'),
        ('Not approved', 'Not approved'),
        ('On hold', 'On hold'),
        ('Closed', 'Closed'),
    )

TASK_CHOICES = (
        ('Scoping and costing', 'Scoping and costing'),
        ('Data retrieval and analysis', 'Data retrieval and analysis'),
        ('Approval', 'Approval'),
    )

PROJECT_TYPE_CHOICES = (
    ('Project', 'Project'),
    ('Request', 'Request')
)


DATA_TYPE_CHOICES = (
    ('Re-identifiable', 'Re-identifiable'),
    ('Aggregated', 'Aggregated')
)

class DataRequest(models.Model):
    request_creator = models.ForeignKey(User, related_name="request_creator", on_delete=models.CASCADE, null=True)
    currently_assigned_to = models.ForeignKey(User, related_name="project", on_delete=models.CASCADE, null=True)
    requestor_contact_name = models.CharField(max_length = 255)
    requestor_contact_email = models.CharField(max_length = 255, blank = True)
    requestor_organisation = models.CharField(max_length = 255, blank = True)
    requestor_organisation_type = models.CharField(max_length = 255, blank = True)
    detail = models.TextField()
    date_received = models.DateField(default=datetime.now, blank=True)
    current_status = models.CharField(max_length=255, choices=STATUS_CHOICES)
    has_associated_cost = models.BooleanField(default = False)
    quoted_cost = models.FloatField(default = 0.00)
    date_due = models.DateField(default=datetime.now, blank=True)
    related_documentation = models.CharField(max_length=255)
    data_type = models.CharField(max_length = 255, choices = DATA_TYPE_CHOICES)
    seeking_contentious_data = models.BooleanField(default = False)
    archived = models.BooleanField(default = False)
