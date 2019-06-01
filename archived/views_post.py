from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from news_items.models import NewsItem
from projects.models import DataRequest
from logs.models import DataUploadLog
from data_assets.models import DataAsset, DataAssetRole
from data_projects.models import DataProject
from . import forms
from .forms import DataRequestForm, TaskEditForm, NoteEditForm
from notes_and_tasks.models import NoteOrTask
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User



# Forms on request page ------------------------------------------------------------------
class NoteFormView(FormView):
    form_class = forms.NoteForm
    template_name = 'main/data-request-detail.html'
    success_url = '/'



    def post(self, request, *args, **kwargs):
        referer = self.request.META.get('HTTP_REFERER')
        request_id = int(referer.split('/')[-2])

        note_form = self.form_class(request.POST)
        task_form = forms.TaskForm()
        updated_status_form = forms.UpdateStatusForm()


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
    form_class = forms.TaskForm
    template_name = 'main/data-request-detail.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        referer = self.request.META.get('HTTP_REFERER')
        request_id = int(referer.split('/')[-2])

        task_form = self.form_class(request.POST)
        note_form = forms.NoteForm()
        updated_status_form = forms.UpdateStatusForm()


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
    form_class = forms.UpdateStatusForm
    template_name = 'main/data-request-detail.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        referer = self.request.META.get('HTTP_REFERER')
        request_id = int(referer.split('/')[-2])

        updated_status_form = self.form_class(request.POST)
        note_form = forms.NoteForm()
        task_form = forms.TaskForm()


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



# Main Request View -----------------------------------------------------------
class DataRequestDetailView(TemplateView):

    template_name = 'main/data-request-detail.html'

    def get(self, request, *args, **kwargs):
        project = get_object_or_404(DataRequest, pk = self.kwargs['var1'])

        note_form = forms.NoteForm(self.request.GET or None)
        task_form = forms.TaskForm(self.request.GET or None)
        updated_status_form = forms.UpdateStatusForm(self.request.GET or None)
        change_task_status_form = forms.ChangeTaskStatusForm(self.request.GET or None)

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
    request_id = str(instance.related_request.id)
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
        return HttpResponseRedirect('/maple/data-requests/' + request_id, {
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

            return HttpResponseRedirect('/cida/thanks', {'form':form})

    else:
        form = DataRequestForm()
    return render(request, 'main/submit-data-request.html', {'form': form})


# Generic thankyou form ----------------------------------------------------------------------
def thanks(request):
	return render(request, 'main/thanks.html')
