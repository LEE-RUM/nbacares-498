from ast import Del
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from .forms import ProjectUpdateForm, AdminUserCreation, AdminUserCreationAdditionalFields, CreateResidentUserForm, ProjectForms, BlogForm
from .models import *
from .models import Blog
from .filters import OrgEventFilter, ContactFilter, CalendarFilter
from .decorators import allowed_users
from django.views import generic
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls.base import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse



def view_home(request):
    return render(request, 'ProjectSite/home.html')

def view_about(request):
    return render(request, 'ProjectSite/about.html')

class view_post(DetailView):
    model = Blog
    template_name = 'ProjectSite/post.html'
    slug_url_kwarg = 'title'
    slug_field = 'slug'
    #query_pk_and_slug = False

def view_blog(request):
    post = Blog.objects.all().order_by('-created_at')
    context = {'post': post}
    return render(request, 'ProjectSite/blog.html', context)

class create_blog(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'ProjectSite/create-blog.html'
    slug_url_kwarg = 'title'
    slug_field = 'slug'
    success_url = reverse_lazy('blog')

    def test_func(self):
        return self.request.user.groups.filter(name='admin')

class edit_blog(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = 'ProjectSite/edit-blog.html'
    slug_url_kwarg = 'title'
    slug_field = 'slug'
    success_url = reverse_lazy('blog')

    def test_func(self):
        return self.request.user.groups.filter(name='admin')

class delete_blog(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    form_class = BlogForm
    template_name = 'ProjectSite/delete-blog.html'
    slug_url_kwarg = 'title'
    slug_field = 'slug'
    success_url = reverse_lazy('blog')

    def test_func(self):
        return self.request.user.groups.filter(name='admin')


def view_resources(request):
    selectedService = "All"

    if request.GET.get("service"):
        selectedService = request.GET.get("service")

    allcontacts = Contact.objects.all()
    conFilters = ContactFilter({'service': selectedService}, queryset=allcontacts)
    filterdContacts = conFilters.qs # filter contacts
    p = Paginator(filterdContacts, 30) # paginator based on filterd contacts
    page = request.GET.get('page')
    pagContacts = p.get_page(page)
    categories = Category.objects.all().order_by('orderingID')
    services = Service.objects.all().order_by('orderingID')
    
    
    context = {'allcontacts': allcontacts, 'conFilters': conFilters, 'categories': categories, 'services': services, 'selectedService': selectedService , 'pagContacts': pagContacts}
    return render(request, 'ProjectSite/resources.html', context)

#Auto suggest function
def autosuggest(request):
    print(request.GET)
    query = request.GET.get('term')
    qs = Service.objects.filter(service__startswith = query)
    mylist = []
    mylist += [x.service for x in qs]
    return JsonResponse(mylist,safe=False)

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


def resident_signup(request):
    form = CreateResidentUserForm()
    if request.method == 'POST':
        form = CreateResidentUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            phone = form.cleaned_data.get('phone')

            group = Group.objects.get(name='resident')
            user.groups.add(group) 
            Resident.objects.create(
                user=user,
                phone=phone,
            )
            login(request, user)
            return redirect('home')

    context = {'form': form}
    return render(request, 'ProjectSite/signup.html', context)

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

def resident_profile(request):
    username = request.user.username
    email = request.user.email
    phone = request.user.resident.phone

    context = { 'username': username, 'email': email, 'phone': phone }
    return render(request, 'ProjectSite/resident/profile.html', context)

def resident_profile_edit(request):
    context = {}
    return render(request, 'ProjectSite/resident/profile-edit.html', context)


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
        forms = self.class_form(request.POST, request.FILES)
        if forms.is_valid():
            form = forms.save(commit=False)
            form.user = Organization.objects.get(user=request.user)
            form.save()
            return redirect('calendar')
        context = {"form": forms}
        return render(request, 'ProjectSite/calendar-template.html', context)