# Generated by Django 5.2 on 2025-04-16 18:58

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shorturl',
            name='time_date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
