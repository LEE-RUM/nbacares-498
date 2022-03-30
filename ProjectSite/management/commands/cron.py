from django.core.management.base import BaseCommand
from ProjectSite.views import send_email_notifications

class Command(BaseCommand):
    # send_email_notifications()
    def handle(self, *args, **options):
        print("hello")
        send_email_notifications()
