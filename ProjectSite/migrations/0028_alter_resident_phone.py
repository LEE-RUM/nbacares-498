# Generated by Django 3.2.8 on 2022-02-15 03:40

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectSite', '0027_resident_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resident',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
    ]
