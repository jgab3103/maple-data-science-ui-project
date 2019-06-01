from rest_framework import serializers
from . import models


class ResearchProjectOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DataProjectOutput
        fields = (
            'data_project',
            'output_title',
            'publication_or_conference_name',
            'summary',
            'start_date',
            'expected_release_date',
            'actual_release_date',
            'output_type',
            'current_status'

        )


class ResearchProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DataProject
        fields = (
             'id',
             'title',
             'summary',
             'research_type',
             'research_type',
             'related_documentation_location',
             'start_date',
             'end_date',
             'internal_investigators_only',
             'current_status'
        )



class ResearchProjectGrantApplicationReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DataProjectGrantApplicationReview
        fields = (
             'id',
             'grant_id',
             'ci_prefix',
             'ci_name',
             'application_title',
             'administering_organisation',
             'lead_organisation',
             'status_of_review'


        )


class ResearchProjectGrantApplicationReviewerScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DataProjectGrantApplicationReviewerScore
        fields = (
             'id',
             'reviewer_name',
             'application',
             'significance_score',
             'team_track_record_score',
             'translation_score',
             'sustainability_score',
             'comments',
             'date_finalised'
        )
