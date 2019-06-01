from django import forms
from django.forms import ModelForm
from projects.models import DataRequest
from data_assets.models import DataAssetBreach
from notes_and_tasks.models import NoteOrTask
from config import app_config


class ChangeTaskStatusForm(forms.Form):
    task_status = forms.ChoiceField(label = "Change status", choices = app_config.STATUS_CHOICES)


class UpdateStatusForm(forms.Form):
    updated_status = forms.ChoiceField(label = "Change status", choices = app_config.STATUS_CHOICES)


class TaskEditForm(ModelForm):
    class Meta:
        model = NoteOrTask
        fields = (
            'created_by',
            'detail',
            'allocated_to',
            'task_completed'
        )


class NoteEditForm(ModelForm):
    class Meta:
        model = NoteOrTask
        fields = (
            'detail',
        )



class DataRequestForm(ModelForm):
    class Meta:
        model = DataRequest
        fields = (
            'requestor_contact_name',
            'data_type',
            'detail',
            'related_documentation',
        )



class DataAssetBreachForm(forms.ModelForm):
	class Meta:
		model = DataAssetBreach
		fields = [
				"date_of_report",
			    "summary",
			    "description"
		]


class NoteForm(ModelForm):
    class Meta:
        model = NoteOrTask
        fields = (
                    'detail',
                )


class TaskForm(ModelForm):
    class Meta:
        model = NoteOrTask
        fields = (
            'allocated_to',
            'detail',
            'date_due',
        )
