# Generated by Django 3.2.8 on 2022-02-06 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectSite', '0012_alter_blog_myvideos'),
    ]

    operations = [
        migrations.AddField(
            model_name='videos',
            name='title',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]