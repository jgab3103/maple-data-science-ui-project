from django.db import models
from django.contrib.auth.models import User
from projects.models import DataRequest
from data_projects.models import DataProjectOutput
from datetime import datetime


TYPE_CHOICES = (
    ("Note", "Note"),
    ("Task", "Task"),
)


class NoteOrTask(models.Model):
    type = models.CharField(max_length=200, choices = TYPE_CHOICES)
    allocated_to = models.ForeignKey(User, related_name = "user_allocated_to", on_delete = models.CASCADE, null = True, blank = True)
    created_by = models.ForeignKey(User, related_name = "user_created_by", on_delete = models.CASCADE, null = True)
    date_and_time_created = models.DateTimeField(auto_now_add=True)
    related_project_output = models.ForeignKey(DataProjectOutput,  on_delete=models.CASCADE, null = True, blank = True)
    related_request = models.ForeignKey(DataRequest, on_delete=models.CASCADE, null = True, blank = True)
    detail = models.TextField(null = True)
    date_due = models.DateField(default=datetime.now, blank=True)
    task_completed = models.BooleanField(default=False)
    restricted_to_admin_staff = models.BooleanField(default=False)

    class Meta:
        ordering = ["-date_and_time_created"]
