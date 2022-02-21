from django.forms import ModelForm, models, DateInput
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import OrgEvent, Organization, Event, Blog
from phonenumber_field.formfields import PhoneNumberField
from django.core.exceptions import ValidationError

#videoChoices = Videos.objects.all().values_list('title', 'title')
#videoChoicesList = []
#for item in videoChoices:
#    videoChoicesList.append(item)

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

class CreateResidentUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3 p-3', 'placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control mb-3 p-3", 'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control mb-3 p-3", 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control mb-3 p-3", 'placeholder': 'Confirm Password'}))
    phone = PhoneNumberField(required=False, widget=forms.TextInput(attrs={'id':'phone', "class":"form-control mb-3 p-3"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'phone')
    
    # make sure the user enterd an unique email
    def clean(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        if User.objects.filter(username=username).exists():
            raise ValidationError("Username taken, use another Username")
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email taken, use another email")

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

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        #fields = ['post_title', 'post', 'image']

        widgets = {
            'post_title': forms.TextInput(attrs={
                'class': 'form-control blog-form',
                'placeholder': "Title"
            }),
            #'post': forms.Textarea(attrs={
            #    'class': 'form-control blog-form',
            #    'placeholder': "Post Content"
            #}),
            #'video_urls': forms.CheckboxSelectMultiple(choices=videoChoicesList, attrs={
            #    'class': 'blog-form',
            #}),
        }

