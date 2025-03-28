# Generated by Django 5.0 on 2025-01-29 06:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
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
        migrations.CreateModel(
            name='IsAuthenticated',
            fields=[
                ('index', models.BigAutoField(db_index=True, primary_key=True, serialize=False)),
                ('isverified', models.BooleanField(default=False, verbose_name='Is Authenticated  ?')),
                ('otp', models.CharField(max_length=6, verbose_name='Otp')),
                ('user', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Verification')),
            ],
        ),
        migrations.DeleteModel(
            name='Otp',
        ),
        migrations.AddField(
            model_name='emailpreferences',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Verification'),
        ),
        migrations.AddField(
            model_name='smsalert',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Verification'),
        ),
    ]
