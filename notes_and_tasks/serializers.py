from rest_framework import serializers
from django.contrib.auth.models import User
from . import models


class NoteOrTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NoteOrTask
        fields = (
        'id',
            'type',
            'allocated_to',
            'date_and_time_created',
            'created_by',
            'related_request',
            'detail',
            'date_due',
            'task_completed',
            'restricted_to_admin_staff'
        )
