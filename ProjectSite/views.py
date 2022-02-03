from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from .forms import ProjectUpdateForm, AdminUserCreation, AdminUserCreationAdditionalFields, ProjectForms
from .models import *
from .filters import OrgEventFilter, ContactFilter, CalendarFilter
from .decorators import allowed_users
from django.views import generic
from django.core.paginator import Paginator

def view_home(request):
    return render(request, 'ProjectSite/home.html')


def view_about(request):
    return render(request, 'ProjectSite/about.html')


def view_resources(request):
    selectedService = "All"
    if request.GET:
        # selectedService = request.GET['service']
        selectedService = request.GET.get('service')

    allcontacts = Contact.objects.all()
    conFilters = ContactFilter({'service': selectedService}, queryset=allcontacts)
    allcontacts = conFilters.qs
    p = Paginator(Contact.objects.all(),30)
    page = request.GET.get('page')
    pagContacts = p.get_page(page)
    categories = Category.objects.all()
    services = Service.objects.all()

    context = {'allcontacts': allcontacts, 'conFilters': conFilters, 'categories': categories, 'services': services, 'selectedService': selectedService , 'pagContacts': pagContacts}
    return render(request, 'ProjectSite/resources.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles='admin')
def view_events(request):
    orgevents = OrgEvent.objects.all()
    completed_events = orgevents.filter(org_event_status='Accepted')

    event_add = ProjectForms()
    if request.method == 'POST':
        event_add = ProjectForms(request.POST)
        if event_add.is_valid():
            event_add.save()
            return redirect('events')

    events = Event.objects.all()
    context = {'events': events, 'event_add': event_add, 'completed_events': completed_events}
    return render(request, 'ProjectSite/events.html', context)


def view_login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('home')
    else:
        login_form = AuthenticationForm()
    context = {'login_form': login_form}
    return render(request, 'ProjectSite/login.html', context)


def view_logout(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def create_events(request, pk):
    EventFormSet = inlineformset_factory(Organization, OrgEvent, fields=('org_event_event', 'org_event_status'),
                                         extra=1)
    organization = Organization.objects.get(id=pk)
    formset = EventFormSet(queryset=OrgEvent.objects.none(), instance=organization)
    if request.method == 'POST':
        formset = EventFormSet(request.POST, instance=organization)
        if formset.is_valid():
            formset.save()
            return redirect('admin_panel')
    context = {'formset': formset}
    return render(request, 'ProjectSite/events-create.html', context)


@login_required(login_url='login')
def update_events(request, pk):
    orgevents = Event.objects.get(id=pk)
    if request.method == 'POST':
        form = ProjectUpdateForm(request.POST, instance=orgevents)
        if form.is_valid():
            form.save()
            return redirect('admin_panel')
    else:
        form = ProjectUpdateForm(instance=orgevents)

    context = {'form': form}
    return render(request, 'ProjectSite/events-update.html', context)


@login_required(login_url='login')
def delete_events(request, pk):
    form = Event.objects.get(id=pk)
    if request.method == 'POST':
        form.delete()
        return redirect('admin_panel')
    context = {'form': form}
    return render(request, 'ProjectSite/events-delete.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles='admin')
def view_admin_panel(request):
    events = Event.objects.all()
    total_events = events.count()
    pending_events = events.filter(event_status='Pending')
    pending_events_Count = events.filter(event_status='Pending').count()
    Accepted_events = events.filter(event_status='Accepted')
    Accepted_events_Count = events.filter(event_status='Accepted').count()
    canceled_events = events.filter(event_status='Canceled')
    orgs = Organization.objects.all()

    context = {'events': events, 'total_events': total_events, 'pending_events': pending_events,
               'pending_events_Count': pending_events_Count, 'Accepted_events': Accepted_events,
               'Accepted_events_Count': Accepted_events_Count, 'orgs': orgs, 'canceled_events': canceled_events}

    return render(request, 'ProjectSite/admin-panel.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles='admin')
def view_admin_organzation(request, pk):
    org = Organization.objects.get(id=pk)
    orgevents = org.event_set.all()
    orgevents_count = orgevents.count()

    OrganizationEventFilter = OrgEventFilter(request.GET, queryset=orgevents)
    orgevents = OrganizationEventFilter.qs
    context = {'org': org, 'orgevents': orgevents, 'orgevents_count': orgevents_count,
               'OrganizationEventFilter': OrganizationEventFilter}
    return render(request, 'ProjectSite/admin-organization.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles='admin')
def view_admin_user_creation(request, *args, **kwargs):
    user_form = AdminUserCreation()
    if request.method == 'POST':
        user_form = AdminUserCreation(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            return redirect('admin_panel')
    context = {'user_form': user_form}
    return render(request, 'ProjectSite/admin-user-creation.html', context)


@login_required(login_url='login')
def view_organization_events(request):
    org = request.user.organization
    orgevents = org.event_set.all()
    context = {'orgevents': orgevents}
    return render(request, 'ProjectSite/organization_events.html', context)


def view_organization_settings(request):
    organ = request.user.organization
    orgevents = organ.event_set.all()
    form = AdminUserCreationAdditionalFields(instance=organ)
    if request.method == 'POST':
        form = AdminUserCreationAdditionalFields(request.POST, instance=organ)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form, 'orgevents': orgevents}
    return render(request, 'ProjectSite/organization-settings.html', context)


class view_calendar(generic.View):
    class_form = ProjectForms

    def get(self, request, *args, **kwargs):
        forms = self.class_form()
        events = Event.objects.all()
        events = events.filter(event_status='Accepted')
        event_list = []
        calendarFilter = CalendarFilter(request.GET, queryset=events)
        events = calendarFilter.qs
        for event in events:
            event_list.append(
                {
                    "title": event.event_name,
                    "start": event.event_sTime.date().strftime("%Y-%m-%dT%H:%M:%S"),
                    "end": event.event_eTime.date().strftime("%Y-%m-%dT%H:%M:%S"),
                }
            )
        context = {'form': forms, 'events': event_list, 'calendarFilter': calendarFilter}
        return render(request, 'ProjectSite/calendar-template.html', context)

    def post(self, request, *args, **kwargs):
        forms = self.class_form(request.POST)
        if forms.is_valid():
            form = forms.save(commit=False)
            form.user = Organization.objects.get(user=request.user)
            form.save()
            return redirect('calendar')
        context = {"form": forms}
        return render(request, 'ProjectSite/calendar-template.html', context)
