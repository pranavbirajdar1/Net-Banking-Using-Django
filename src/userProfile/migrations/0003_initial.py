# Generated by Django 5.0 on 2025-01-29 07:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userProfile', '0002_delete_myappmodel'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPreference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailnotification', models.CharField(blank=True, max_length=30, null=True, verbose_name='Email Notifications')),
                ('smsnotification', models.CharField(blank=True, max_length=30, null=True, verbose_name='SMS Notifications')),
                ('user', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Verification')),
            ],
        ),
    ]
