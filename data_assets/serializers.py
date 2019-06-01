from rest_framework import serializers
from . import models


class DataAssetBreachSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DataAssetBreach
        fields = (
         'date_of_report',
         'summary',


        )


class DataAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DataAsset
        fields = (
            'owning_org',
            'owning_business_unit',
            'name',
            'asset_id',
            'version',
            'type',
            'emergency_shutdown_org',
            'emergency_shutdown_contact',
            'start_date',
            'end_date',
            'data_sensitivity_level',
            'update_frequency',
            'currently_active',
            'utlizes_external_data',
            'governed_as_external_data',
            'available_for_analytics',
            'under_review',
            'used_in_shared_dictionary',
            'usage_notes',
            'data_location_type',
            'data_location',
            'description',
            'supporting_documentation',



        )
