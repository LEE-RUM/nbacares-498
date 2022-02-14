from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Organization


# @receiver(post_save, sender=User)
# def create_or_update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         group = Group.objects.get(name='organizer')
#         instance.groups.add(group)
#         Organization.objects.create(user=instance, org_name=instance.username)
#         #profile = Organization(user=instance) WORKING
#     instance.organization.save()


"""
https://stackoverflow.com/questions/66491021/doesnotexist-getting-group-matching-query-does-not-exist-error-while-saving
"""