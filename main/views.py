from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Avg, Variance
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import TemplateView, FormView
import django_filters

from . import filters
from . import forms
from .forms import DataRequestForm, TaskEditForm, NoteEditForm, NoteForm, TaskForm, UpdateStatusForm, ChangeTaskStatusForm
from apps_and_notebooks.models import AppOrNotebook
from data_assets.models import DataAsset, DataAssetRole
from data_api.models import DataAPI
from data_projects.models import DataProject, DataProjectGrantApplicationReview, DataProjectInvestigator, DataProjectOutputInvestigator, DataProjectOutput
from logs.models import DataUploadLog
from news_items.models import NewsItem
from projects.models import DataRequest
from notes_and_tasks.models import NoteOrTask




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
    news_items = NewsItem.objects.filter(is_displayed = True).order_by('-date_added')[0:3]
    context = {'news_items': news_items,
                'task_count': task_count}
    return render(request, 'main/index.html', context)


def data_api(request):
    data_apis = DataAPI.objects.all()
    context = {"data_apis":data_apis}
    return render(request, 'main/data-api.html', context)


def metadata(request):
    data_assets = DataAsset.objects.filter(currently_active = True).order_by('name')
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
    user_list = DataRequest.objects.filter(archived = False)
    user_filter = filters.DataRequestFilter(request.GET, queryset=user_list)
    user_list = user_filter.qs

    paginator = Paginator(user_list, 20)
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
    all_projects = DataProject.objects.filter(archived=False)
    paginator = Paginator(all_projects, 30)
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



def data_projects_detail(request, data_project_id):
    data_project = get_object_or_404(DataProject, pk = data_project_id)
    return render(request, 'main/data_project_detail.html', {"data_project": data_project})



def data_projects_review_detail(request, data_project_id):
    grant_review = get_object_or_404(DataProjectGrantApplicationReview, pk = data_project_id)
    return render(request, 'main/data-project-review-detail.html', {"grant_review": grant_review})

def forms(request):
	return render(request, 'main/forms.html')

def news_item(request, news_item_id):
    news = get_object_or_404(NewsItem, pk=news_item_id)
    return render(request, 'main/news.html', {"news": news})




# Forms on request page ------------------------------------------------------------------
class NoteFormView(FormView):
    form_class = NoteForm
    template_name = 'main/data-request-detail.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        referer = self.request.META.get('HTTP_REFERER')
        request_id = int(referer.split('/')[-2])

        note_form = self.form_class(request.POST)
        task_form = TaskForm
        updated_status_form = UpdateStatusForm


        if note_form.is_valid():
            note = NoteOrTask(
                    type = "Note",
                    allocated_to = request.user,
                    created_by = request.user,
                    related_request = get_object_or_404(DataRequest, pk = request_id),
                    detail = note_form.data['detail'],
                    date_due = timezone.now(),
                    task_completed = False,
                    restricted_to_admin_staff = False,
                )
            note.save()
            return HttpResponseRedirect('/maple/data-requests/' + str(request_id))
        else:
            return self.render_to_response(
                self.get_context_data(
                    note_form=note_form,
                    task_form=task_form,
                    updated_status_form = updated_status_form,

                )
            )


class TaskFormView(FormView):
    form_class = TaskForm
    template_name = 'main/data-request-detail.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        referer = self.request.META.get('HTTP_REFERER')
        request_id = int(referer.split('/')[-2])

        task_form = self.form_class(request.POST)
        note_form = NoteForm
        updated_status_form = UpdateStatusForm


        if task_form.is_valid():
            task = NoteOrTask(
                    type = "Task",
                    allocated_to = get_object_or_404(User, pk = task_form.data['allocated_to']),
                    created_by = request.user,
                    related_request = get_object_or_404(DataRequest, pk = request_id),
                    detail = task_form.data['detail'],
                    date_due = task_form.data['date_due'],
                    task_completed = False,
                    restricted_to_admin_staff = False,
                )
            task.save()
            return HttpResponseRedirect('/maple/data-requests/' + str(request_id))
        else:
            return self.render_to_response(
                self.get_context_data(
                    task_form=task_form,
                    note_form=note_form,
                    updated_status_form = updated_status_form,

                )
            )

class UpdateStatusFormView(FormView):
    form_class = UpdateStatusForm
    template_name = 'main/data-request-detail.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        referer = self.request.META.get('HTTP_REFERER')
        request_id = int(referer.split('/')[-2])

        updated_status_form = self.form_class(request.POST)
        note_form = NoteForm
        task_form = TaskForm


        if updated_status_form.is_valid():
            DataRequest.objects.filter(pk=request_id).update(current_status=updated_status_form.data['updated_status'])
            note = NoteOrTask(
                        type = "Note",
                                allocated_to = request.user,
                                created_by = request.user,
                                related_request = get_object_or_404(DataRequest, pk = request_id),
                                detail = "Status of request changed to \"" + updated_status_form.data['updated_status'] + "\"",
                                date_due = timezone.now(),
                                task_completed = False,
                                restricted_to_admin_staff = False,
                            )
            note.save()

            return HttpResponseRedirect('/maple/data-requests/' + str(request_id))
        else:
            return self.render_to_response(
                self.get_context_data(
                    task_form=task_form,
                    note_form=note_form,
                    updated_status_form = updated_status_form,

                )
            )




class DataProjectOutputNoteFormView(FormView):
    form_class = NoteForm
    template_name = "main/data-project-output-detail.html"
    success_url = '/'

    def post(self, request, *args, **kwargs):
        referer = self.request.META.get('HTTP_REFERER')
        request_id = int(referer.split('/')[-2])

        note_form = self.form_class(request.POST)
        task_form = TaskForm
        updated_status_form = UpdateStatusForm


        if note_form.is_valid():
            note = NoteOrTask(
                    type = "Note",
                    allocated_to = request.user,
                    created_by = request.user,
                    related_project_output = get_object_or_404(DataProjectOutput, pk = request_id),

                    detail = note_form.data['detail'],
                    date_due = timezone.now(),
                    task_completed = False,
                    restricted_to_admin_staff = False,
                )
            note.save()
            return HttpResponseRedirect('/maple/data-project-output/'  + str(request_id))
        else:
            return self.render_to_response(
                self.get_context_data(
                    note_form=note_form,

                )
            )

class DataProjectOutputDetailView(TemplateView):
    template_name = "main/data-project-output-detail.html"
    def get(self, request, *args, **kwargs):
        project = get_object_or_404(DataProjectOutput, pk = self.kwargs['var1'])
        note_form = NoteForm(self.request.GET or None)
        context = self.get_context_data(**kwargs)
        context = {
        'project': project,
        'note_form' : note_form,

        }
        return self.render_to_response(context)


# Main Request View -----------------------------------------------------------
class DataRequestDetailView(TemplateView):

    template_name = 'main/data-request-detail.html'

    def get(self, request, *args, **kwargs):
        project = get_object_or_404(DataRequest, pk = self.kwargs['var1'])

        note_form = NoteForm(self.request.GET or None)
        task_form = TaskForm(self.request.GET or None)
        updated_status_form = UpdateStatusForm(self.request.GET or None)
        change_task_status_form = ChangeTaskStatusForm(self.request.GET or None)

        context = self.get_context_data(**kwargs)
        context = {
        'task_form' : task_form,
        'note_form' : note_form,
        'project': project,
        'updated_status_form': updated_status_form,
        'change_task_status_form': change_task_status_form
        }

        return self.render_to_response(context)






def edit_task_or_note(request, id):
    instance = get_object_or_404(NoteOrTask, id=id)
    try:
        request_id = str(instance.related_request.id)
        is_request = True
    except:
        pass
    try:
        request_id = str(instance.related_project_output.id)
        is_request = False
    except:
        pass
    task_edit_form = TaskEditForm(request.POST or None, instance=instance)
    note_edit_form = NoteEditForm(request.POST or None, instance = instance)
    if task_edit_form.is_valid():
        task_edit_form.save()
        return HttpResponseRedirect('/maple/data-requests/' + request_id, {
        'note_edit_form' : 'note_edit_form',
        'form':task_edit_form,
        'instance': instance})
    if note_edit_form.is_valid():
        note_edit_form.save()
        if is_request == True:
            redirect_str = '/maple/data-requests/'
        else:
            redirect_str = '/maple/data-project-output/'
        return HttpResponseRedirect(redirect_str + request_id, {
            'note_edit_form' : 'note_edit_form',
            'form':task_edit_form,
            'instance': instance})
    return render(request, 'main/task-note-edit.html', {'form': task_edit_form,
    'instance':instance, 'note_edit_form' : note_edit_form})

#####
def submit_data_request(request):
    if request.method == 'POST':
        form = DataRequestForm(request.POST)
        if form.is_valid():
            dataRequest = DataRequest(
                request_creator = User.objects.get(id=1),
                currently_assigned_to = User.objects.get(id=1),
                requestor_contact_name = form.data['requestor_contact_name'],
                requestor_organisation = "Not available",
                requestor_contact_email = "Not available",
                requestor_organisation_type = "Not available",
                detail = form.data['detail'],
                date_received = timezone.now(),
                current_status = "Awaiting triage",
                has_associated_cost = False,
                quoted_cost = 1.0,
                date_due = timezone.now() +  timezone.timedelta(days=7),
                related_documentation = form.data['related_documentation'],
                data_type = form.data['data_type']

            )

            dataRequest.save()

            linkText = '<span>You can link directly to this request <a href = "/maple/data-requests/' + str(dataRequest.id) + '">here.</a></span>'
            messages.error(request, linkText, extra_tags='safe')

            return HttpResponseRedirect('/maple/thanks', {'form':form})

    else:
        form = DataRequestForm()
    return render(request, 'main/submit-data-request.html', {'form': form})


# Generic thankyou form ----------------------------------------------------------------------
def thanks(request):
	return render(request, 'main/thanks.html')
