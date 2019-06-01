from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

class AppOrNotebook(models.Model):
    created_by = models.ForeignKey(User, related_name="app_or_notebook", on_delete=models.CASCADE,
                              null=True)
    title = models.CharField(max_length=255)
    release_date = models.DateField(default=datetime.now)
    description = models.TextField()
    location = models.CharField(max_length=255)
    tags = models.CharField(max_length = 255)
    version = models.FloatField()
    type = models.CharField(max_length = 50)

    def __str__(self):
        return self.title
