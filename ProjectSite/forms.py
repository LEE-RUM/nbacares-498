from django.forms import ModelForm, models, DateInput
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import OrgEvent, Organization, Event


class AdminUserCreation(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class AdminUserCreationAdditionalFields(models.ModelForm):
    class Meta:
        model = Organization
        fields = ['org_name', 'org_address', 'org_phone', 'org_email']

        widgets = {
            'org_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'org_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Address'}),
            'org_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
            'org_email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
        }


class ProjectUpdateForm(ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'event_description', 'event_tag', 'event_status']


class ProjectForms(ModelForm):
    class Meta:
        CHOICES = (('None', 'None'), ('Toddler', 'Toddler'),
                   ('Child', 'Child'), ('Adolescent', 'Adolescent'), ('Adult', 'Adult'),
                   ('Elderly', 'Elderly'), ('Other', 'Other'))
        model = Event
        fields = ['event_name', 'event_description', 'event_sTime', 'event_eTime', 'event_tag']

        widgets = {
            'event_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter event title'}),
            'event_description': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Enter event description'}),
            'event_sTime': DateInput(attrs={'type': 'datetime-local', 'class': 'form-control'},
                                     format="%Y-%m-%dT%H:%M", ),
            'event_eTime': DateInput(attrs={'type': 'datetime-local', 'class': 'form-control'},
                                     format="%Y-%m-%dT%H:%M", ),
            'event-tag': forms.ChoiceField(choices=CHOICES),
        }
        exclude = ['event_date_created']

    def __init__(self, *args, **kwargs):
        super(ProjectForms, self).__init__(*args, **kwargs)
        self.fields["event_sTime"].input_formats = ("%Y-%m-%dT%H:%M",)
        self.fields["event_eTime"].input_formats = ("%Y-%m-%dT%H:%M",)
