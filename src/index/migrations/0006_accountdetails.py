# Generated by Django 5.0 on 2025-01-22 08:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_isauthenticated'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountDetails',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('account_number', models.CharField(max_length=20, verbose_name='Account Number')),
                ('account_status', models.CharField(max_length=20, verbose_name='Account Status')),
                ('account_balance', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Account')),
                ('ifsc', models.CharField(default='LACF0001234', max_length=11, verbose_name='IFSC CODE')),
                ('user', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Account Details')),
            ],
        ),
    ]
