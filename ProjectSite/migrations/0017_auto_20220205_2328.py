# Generated by Django 3.2.8 on 2022-02-06 04:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectSite', '0016_auto_20220205_2325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videos',
            name='blog',
        ),
        migrations.AddField(
            model_name='blog',
            name='myvideos',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ProjectSite.videos'),
        ),
    ]