# Generated by Django 3.2.3 on 2021-05-23 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='about',
            field=models.TextField(default='blank'),
            preserve_default=False,
        ),
    ]
