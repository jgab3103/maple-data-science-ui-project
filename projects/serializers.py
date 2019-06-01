from rest_framework import serializers
from django.contrib.auth.models import User
from . import models
from notes_and_tasks.models import NoteOrTask

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name'
        )


class NoteOrTaskSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = NoteOrTask
        fields = ('allocated_to',
                'type',
                'created_by',
                'date_and_time_created',
                'detail',
                'date_due',
                'task_completed',)



class RequestSerializer(serializers.ModelSerializer):
    note_or_tasks = NoteOrTaskSerializer(many=True, read_only=True)
    class Meta:
        model = models.DataRequest
        fields = (
        'id',
         'request_creator',
         'requestor_contact_name',
         'requestor_contact_email',
         'requestor_organisation',
         'requestor_organisation_type',
         'has_associated_cost',
         'related_documentation',
         'data_type',
         'seeking_contentious_data',
         'detail',
         'current_status',
         'date_received',
         'note_or_tasks',
        )
