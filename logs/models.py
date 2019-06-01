from django.db import models

LOG_STATUS_CHOICES = (
    ("OK", "OK"),
    ("Fail", "Fail"),
    ("Landed", "Landed"),
    ("Staged", "Staged"),
)

class DataUploadLog(models.Model):
    date = models.DateTimeField(auto_now = True)
    message = models.TextField()
    status = models.CharField(max_length = 50, choices = LOG_STATUS_CHOICES)
