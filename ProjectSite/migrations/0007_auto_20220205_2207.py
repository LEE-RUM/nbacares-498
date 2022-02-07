# Generated by Django 3.2.8 on 2022-02-06 03:07

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectSite', '0006_auto_20220204_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(default='', editable=False),
        ),
        migrations.AddField(
            model_name='blog',
            name='video_url',
            field=embed_video.fields.EmbedVideoField(blank=True, null=True),
        ),
    ]
