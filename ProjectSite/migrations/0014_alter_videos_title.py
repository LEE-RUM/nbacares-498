# Generated by Django 3.2.8 on 2022-02-06 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectSite', '0013_videos_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='title',
            field=models.CharField(default='video', max_length=128, null=True),
        ),
    ]