# Generated by Django 4.0.2 on 2022-03-02 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectSite', '0042_galleryimages'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='interested',
            field=models.ManyToManyField(blank=True, default=None, to='ProjectSite.Resident'),
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(choices=[('Interested', 'Interested'), ('Not Interested', 'Not Interested')], default='Not Interested', max_length=15)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProjectSite.event')),
                ('resident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProjectSite.resident')),
            ],
        ),
    ]