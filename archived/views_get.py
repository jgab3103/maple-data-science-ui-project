import django_filters
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.db.models import Avg, Variance
from django.core.paginator import Paginator


from . import filters

from news_items.models import NewsItem
from projects.models import DataRequest
from logs.models import DataUploadLog
from data_assets.models import DataAsset, DataAssetRole
from apps_and_notebooks.models import AppOrNotebook
from data_api.models import DataAPI

from data_projects.models import DataProject, DataProjectGrantApplicationReview, DataProjectInvestigator, DataProjectOutputInvestigator
from notes_and_tasks.models import NoteOrTask
from . import models


@login_required
def user_profile(request):
    task_count = NoteOrTask.objects.filter(allocated_to = request.user,
                                           type = "Task",
                                           task_completed = False)


    data_projects =  DataProjectInvestigator.objects.filter(investigator_name = request.user)
    reporting_outputs_of_user = DataProjectOutputInvestigator.objects.filter(investigator_name = request.user)
    context = {
        'task_count': task_count,
        'data_projects': data_projects,
        'reporting_outputs_of_user' : reporting_outputs_of_user
    }
    return render(request, 'main/user-profile.html', context)


def index(request):
    try:
        task_count = NoteOrTask.objects.filter(allocated_to = request.user).count()
    except:
        task_count= 0
    news_items = NewsItem.objects.filter(is_displayed = True).order_by('-date_added')
    context = {'news_items': news_items,
                'task_count': task_count}
    return render(request, 'main/index.html', context)


def data_api(request):
    data_apis = DataAPI.objects.all()
    context = {"data_apis":data_apis}
    return render(request, 'main/data-api.html', context)


def metadata(request):
    data_assets = DataAsset.objects.all().order_by('name')
    context = {"data_assets" : data_assets}
    return render(request, 'main/metadata.html', context)

def metadata_detail(request, asset_id):
    asset = get_object_or_404(DataAsset, pk = asset_id)
    return render(request, 'main/metadata_detail.html', {"asset": asset})


@login_required
def dataonboarding(request):
    logs = DataUploadLog.objects.filter(status="Staged").order_by('-date')
    context = {'logs': logs}
    return render(request, 'main/data_onboarding.html', context)

def data_requests(request):
    user_list = DataRequest.objects.all()
    user_filter = filters.DataRequestFilter(request.GET, queryset=user_list)
    user_list = user_filter.qs

    paginator = Paginator(user_list, 2)
    page = request.GET.get('page', 1)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    args = {'paginator': paginator,'filter':user_filter,
           'users':users,}
    return render(request, 'main/data-requests.html', args)


def resources(request):
	return render(request, 'main/resources.html')



def apps_and_notebooks(request):
    apps_and_notebooks = AppOrNotebook.objects.all()
    context = {"apps_and_notebooks" : apps_and_notebooks}
    return render(request, 'main/apps_and_notebooks.html', context)


@login_required
def data_projects(request):

    all_projects = DataProject.objects.all()
    paginator = Paginator(all_projects, 5)
    page = request.GET.get('page')
    data_projects = paginator.get_page(page)
    context = {"data_projects" : data_projects}
    return render(request, 'main/data_projects.html', context)


@login_required
def data_project_review(request):
    reviews = DataProjectGrantApplicationReview.objects.all()

    for stuff in reviews:
        try:
            stuff.significance_score_avg = stuff.dataprojectgrantapplicationreviewerscore_set.aggregate(Avg('significance_score'))['significance_score__avg']
            stuff.team_track_record_score_avg = stuff.dataprojectgrantapplicationreviewerscore_set.aggregate(Avg('team_track_record_score'))['team_track_record_score__avg']
            stuff.translation_score_avg = stuff.dataprojectgrantapplicationreviewerscore_set.aggregate(Avg('translation_score'))['translation_score__avg']
            stuff.sustainability_score_avg = stuff.dataprojectgrantapplicationreviewerscore_set.aggregate(Avg('sustainability_score'))['sustainability_score__avg']
            stuff.review_count = stuff.dataprojectgrantapplicationreviewerscore_set.count()
            stuff.total_score = float(stuff.significance_score_avg) + float(stuff.team_track_record_score_avg) + float(stuff.translation_score_avg) + float(stuff.sustainability_score_avg)
        except:
            stuff.total_score = 0
            stuff.no_reviews = True


    context = {"reviews": reviews}


    return render(request, 'main/data-project-review.html', context)


@login_required
def data_projects_detail(request, data_project_id):
    data_project = get_object_or_404(DataProject, pk = data_project_id)
    return render(request, 'main/data_project_detail.html', {"data_project": data_project})


@login_required
def data_projects_review_detail(request, data_project_id):
    grant_review = get_object_or_404(DataProjectGrantApplicationReview, pk = data_project_id)
    return render(request, 'main/data-project-review-detail.html', {"grant_review": grant_review})

def forms(request):
	return render(request, 'main/forms.html')

def news_item(request, news_item_id):
    news = get_object_or_404(NewsItem, pk=news_item_id)
    return render(request, 'main/news.html', {"news": news})
