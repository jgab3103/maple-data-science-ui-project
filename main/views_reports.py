import csv
from django.http import HttpResponse
from . import models
import time
import datetime
from data_assets.models import DataAsset, DataAssetRole



def assets_report(request):

    assets = DataAsset.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data_assets_report.csv"'
    writer = csv.writer(response)
    try:
        writer.writerow(['Report downloaded on: ' + str(datetime.datetime.now()) + " by " + request.user.first_name + " " + request.user.last_name])
    except:
        writer.writerow(['Report downloaded on: ' + str(datetime.datetime.now())])
    writer.writerow(['owning_org',
    'owning_business_unit',
    'name',
    'asset_id',
    'version',
    'type',
    'emergency_shutdown_org',
    'emergency_shutdown_contact',
    'start_date',
    'end_date',
    'data_limiting_marker',
    'update_frequency',
    'currently_active',
    'utlizes_external_data',
    'governed_as_external_data',
    'available_for_analytics',
    'under_review',
    'data_location_type',
    'data_location',
    'supporting_documentation',
    'description',
    ])

    for asset in assets:
        writer.writerow([
        asset.owning_org,
        asset.owning_business_unit,
        asset.name,
        asset.asset_id,
        asset.version,
        asset.type,
        asset.emergency_shutdown_org,
        asset.emergency_shutdown_contact,
        asset.start_date,
        asset.end_date,
        asset.data_limiting_marker,
        asset.update_frequency,
        asset.currently_active,
        asset.utlizes_external_data,
        asset.governed_as_external_data,
        asset.available_for_analytics,
        asset.under_review,
        asset.data_location_type,
        asset.data_location,
        asset.supporting_documentation,
        asset.description
        ])

    return response

def users_report(request):
    users = DataAssetRole.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users_and_roles_report.csv"'
    writer = csv.writer(response)
    try:
        writer.writerow(['Report downloaded on: ' + str(datetime.datetime.now()) + " by " + request.user.first_name + " " + request.user.last_name])
    except:
        writer.writerow(['Report downloaded on: ' + str(datetime.datetime.now())])
    writer.writerow(['first_name',
    'last_name',
    'data_asset_name',
    'type',
    'status',
    'start_date',
    'end_date'])

    for user in users:
        writer.writerow([
        user.user.first_name,
        user.user.last_name,
        user.data_asset.name,
        user.type,
        user.status,
        user.start_date,
        user.end_date
        ])

    return response


# def requests_and_projects_report(request):
#
#     requests_or_projects = models.Project.objects.all()
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="requests_and_projects_report.csv"'
#     writer = csv.writer(response)
#     try:
#         writer.writerow(['Report downloaded on: ' + str(datetime.datetime.now()) + " by " + request.user.first_name + " " + request.user.last_name])
#     except:
#         writer.writerow(['Report downloaded on: ' + str(datetime.datetime.now())])
#     writer.writerow([
#     'current_request_manager',
#     'requestor_contact_name',
#     'requestor_contact_email',
#     'requestor_organisation',
#     'requestor_organisation_type',
#     'title_or_summary',
#     'detail',
#     'date_received',
#     'current_status',
#     'has_associated_cost',
#     'quoted_cost',
#     'date_due',
#     'related_documentation',
#     'project_type',
#     'data_type',
#     ])
#
#     for item in requests_or_projects:
#         writer.writerow([
#         item.current_request_manager,
#         item.requestor_contact_name,
#         item.requestor_contact_email,
#         item.requestor_organisation,
#         item.requestor_organisation_type,
#         item.title_or_summary,
#         item.detail,
#         item.date_received,
#         item.current_status,
#         item.has_associated_cost,
#         item.quoted_cost,
#         item.date_due,
#         item.related_documentation,
#         item.project_type,
#         item.data_type
#
#         ])
#
#     return response
