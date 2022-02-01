from django.db import models

from django.contrib.auth.models import User


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


class Contact(models.Model):
    domains = (
        ('After-school', 'After-school'), ('Art', 'Art'), ('Babysitting', 'Babysitting'), ('Baseball', 'Baseball'),
        ('Culinary', 'Culinary'), ('Dance', 'Dance'), ('Engineering', 'Engineering'), ('Fashion', 'Fashion'),
        ('Football', 'Football'), ('Gardening & Nutrition', 'Gardening & Nutrition'), ('Gymnastics', 'Gymnastics'),
        ('Karate', 'Karate'), ('Leadership', 'Leadership'), ('Literacy', 'Literacy'), ('Music', 'Music'),
        ('Nature', 'Nature'),
        ('Science and Engineering', 'Science and Engineering'), ('Soccer', 'Soccer'), ('Softball', 'Softball'),
        ('Sports', 'Sports'), ('Theatre', 'Theatre'), ('Wrestling', 'Wrestling'),
        ('Summer Camp/Activities', 'Summer Camp/Activities'), ('Summer Employment', 'Summer Employment'),
        ('Adult Mental Health', 'Adult Mental Health'), ('Adult Residential', 'Adult Residential'),
        ('Alternative Education', 'Alternative Education'), ('Behavioral Health', 'Behavioral Health'),
        ('Case Management', 'Case Management'), ('Children\'s Outpatient', 'Children\'s Outpatient'),
        ('Children\'s Group Care', 'Children\'s Group Care'), ('Children\'s Intensive', 'Children\'s Intensive'),
        ('Family Services', 'Family Services'), ('Parenting Groups', 'Parenting Groups'),
        ('Substance Abuse', 'Substance Abuse'), ('Autism', 'Autism'),
        ('Childcare & Preschool', 'Childcare & Preschool'),
        ('College Readiness', 'College Readiness'), ('Community Engagement', 'Community Engagement'),
        ('People with Disabilities', 'People with Disabilities'), ('Domestic Violence', 'Domestic Violence'),
        ('Educational Advocacy', 'Educational Advocacy'), ('Elderly Services', 'Elderly Services'),
        ('Employment', 'Employment'), ('Employment (Youth)', 'Employment (Youth)'),
        ('ESL (English 2ndLanguage)', 'ESL (English 2ndLanguage)'),
        ('Financial Lit. & Assist.', 'Financial Lit. & Assist.'),
        ('G.E.D Programs', 'G.E.D Programs'), ('Housing', 'Housing'), ('Immigrant Resources', 'Immigrant Resources'),
        ('Legal Aide', 'Legal Aide'), ('Literacy', 'Literacy'), ('Mentoring', 'Mentoring'),
        ('Pregnancy Prevention', 'Pregnancy Prevention'), ('Transportation', 'Transportation'),
        ('Tutoring', 'Tutoring'),
        ('Veteran Services', 'Veteran Services'),
    )
    services = models.CharField(max_length=30, null=True, choices=domains)
    contact_resource_provider = models.CharField(max_length=50)
    contact_ages = models.CharField(max_length=20)
    contact_websites = models.CharField(max_length=40, null=True, )
    contact_location = models.CharField(max_length=45)
    contact_number = models.CharField(max_length=18)

    def __str__(self):
        return self.contact_resource_provider
