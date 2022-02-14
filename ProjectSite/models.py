from operator import mod
from django.db import models

from django.contrib.auth.models import User
from django.utils.text import slugify
import itertools

from ckeditor_uploader.fields import RichTextUploadingField

class Organization(models.Model):
    ORGANIZATION_STATUS = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    org_name = models.CharField(max_length=40, null=True, blank=False)
    org_address = models.CharField(max_length=60, null=True, blank=True)
    org_phone = models.CharField(max_length=20, null=True, blank=True)
    org_email = models.EmailField(null=True, blank=True)
    org_status = models.CharField(max_length=20, choices=ORGANIZATION_STATUS, default='Active')
    org_date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.user)

class Resident(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.user.username


class Event(models.Model):
    EVENT_TAGS = (
        ('Housing', 'Housing'), ('Employment', 'Employment'), ('Education', 'Education'),
        ('Financial Literacy', 'Financial Literacy'), ('Healthcare', 'Healthcare'), ('Mental Health', 'Mental Health'),
        ('Family Engagement', 'Family Engagement'), ('Children Activities', 'Children Activities'), ('Art', 'Art'),
        ('Community Event', 'Community Event'), ('Fundraising', 'Fundraising'), ('Other', 'Other'),
    )
    EVENT_STATUS = (
        (u'Accepted', u'Accepted'),
        (u'Pending', u'Pending'),
        (u'Canceled', u'Canceled'),
        (u'Requested For Change', u'Requested For Change'),
    )
    user = models.ForeignKey(Organization, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=100, null=True, blank=False)
    event_description = models.TextField(max_length=400, null=True, blank=True)
    event_sTime = models.DateTimeField()
    event_eTime = models.DateTimeField()
    event_tag = models.CharField(max_length=30, null=True, choices=EVENT_TAGS)
    event_status = models.CharField(max_length=30, choices=EVENT_STATUS, default='Pending')
    event_date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.event_name


class OrgEvent(models.Model):
    EVENT_STATUS = (
        ('Accepted', 'Accepted'),
        ('Waiting Approval', 'Waiting Approval'),
    )
    org_event_organization = models.ForeignKey(Organization, null=True, on_delete=models.SET_NULL)
    org_event_event = models.ForeignKey(Event, null=True, on_delete=models.SET_NULL)
    org_event_status = models.CharField(max_length=20, null=True, choices=EVENT_STATUS)
    org_event_date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.org_event_event.event_name)

class Category(models.Model):
    category = models.CharField(max_length=30, primary_key=True)
    orderingID = models.IntegerField(default=1)

    def __str__(self):
        return self.category

class Service(models.Model):
    service = models.CharField(max_length=30, primary_key=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    orderingID = models.IntegerField(default=1)

    def __str__(self):
        return self.service

class Contact(models.Model):
    
    service = models.ForeignKey(Service, null=True, on_delete=models.CASCADE)
    contact_resource_provider = models.CharField(max_length=50)
    # contact_ages = models.CharField(max_length=20)
    contact_websites = models.CharField(max_length=128, blank=True, null=True)
    # contact_location = models.CharField(max_length=45)
    contact_number = models.CharField(max_length=36, blank=True, null=True )

    def __str__(self):
        return self.contact_resource_provider

class Blog(models.Model):

    post_title = models.CharField(max_length=200)
    post = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    slug = models.SlugField(
        default='',
        editable=False,
    )

    post_content = RichTextUploadingField(null=True, default=True)

    #test2 = RichTextUploadingField(null=True, default=True,external_plugin_resources=[('youtube', 'static/ckeditor/plugins/youtube/youtube/', 'plugin.js')])

    main_image = models.ImageField(upload_to="images/", null=True)

    def __str__(self):
        return self.post_title

    def _generate_slug(self):
        value = self.post_title
        slug_candidate = slug_original = slugify(value, allow_unicode=True)
        for i in itertools.count(1):
            if not Blog.objects.filter(slug=slug_candidate).exists():
                break
            slug_candidate = '{}-{}'.format(slug_original, i)

        self.slug = slug_candidate

    def save(self, *args, **kwargs):
        if not self.pk:
            self._generate_slug()
        super().save(*args, **kwargs)