from django.db import models
from django.contrib.auth.models import User
from datetime import datetime



class DataAPI(models.Model):
    managed_by = models.ForeignKey(User, related_name="data_api", on_delete=models.CASCADE,
                              null=True)
    title = models.CharField(max_length=255)
    version = models.FloatField()
    usage_notes = models.TextField()
    location = models.CharField(max_length=255)
    type = models.CharField(max_length = 255)
    formats_supported = models.CharField(max_length = 255)

    def __str__(self):
        return self.title


class ChangeLog(models.Model):
    data_api = models.ForeignKey(DataAPI, on_delete=models.CASCADE, null = True, blank = True)
    change_details = models.TextField()
    change_date = models.DateField(default=datetime.now, blank=True)
    change_made_by = models.ForeignKey(User, related_name="change_log", on_delete=models.CASCADE,
                              null=True)
