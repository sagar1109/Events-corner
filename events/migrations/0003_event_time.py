# Generated by Django 3.2.3 on 2021-05-23 06:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
