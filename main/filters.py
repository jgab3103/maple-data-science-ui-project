import django_filters
from projects.models import DataRequest
from data_projects.models import DataProjectGrantApplicationReview
from django.db import models
from django import forms
from config import app_config
from django_filters.widgets import RangeWidget
from django.views.generic.list import ListView


class DataProjectReviewFilter(django_filters.FilterSet):
    grant_type = django_filters.ChoiceFilter(
        field_name = "grant_type",
        label = "Grant type",
        choices = app_config.DATA_TYPE_CHOICES
    )
    grant_scheme = django_filters.ChoiceFilter(
        field_name = "grant_scheme",
        label = "Grant scheme",
        choices = app_config.DATA_TYPE_CHOICES
    )
    grant_year = django_filters.ChoiceFilter(
        field_name = "grant_year",
        label = "Grant year",
        choices = app_config.DATA_TYPE_CHOICES
    )

    class Meta:
        model = DataProjectGrantApplicationReview
        fields = ['grant_type',]



class DataRequestFilter(django_filters.FilterSet):
    requestor_contact_name = django_filters.CharFilter(lookup_expr='icontains')
    detail = django_filters.CharFilter(lookup_expr='icontains')
    data_type = django_filters.ChoiceFilter(
        field_name = "data_type",
        label = "Data type",
        choices = app_config.DATA_TYPE_CHOICES
    )
    current_status = django_filters.ChoiceFilter(
        field_name = "current_status",
        label = "Current status",
        choices = app_config.STATUS_CHOICES
    )
    # Datepicker class not operational
    date_received = django_filters.DateFromToRangeFilter(
        field_name = "date_received",
        label = "Date recieved range (YYYY-MM-DD)",
        widget=RangeWidget(
            attrs={
                'class': '_datepicker'
            }
        )
    )
    # Datepicker class not operational
    date_due = django_filters.DateFromToRangeFilter(
                field_name = "date_due",
                label = "Date due range (YYYY-MM-DD)",
                widget=RangeWidget(
                    attrs={
                        'class': '_datepicker'
                    }
                )
            )

    class Meta:
        model = DataRequest
        fields = []
