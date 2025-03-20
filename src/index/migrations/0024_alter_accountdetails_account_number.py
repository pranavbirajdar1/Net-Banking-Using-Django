# Generated by Django 5.1.7 on 2025-03-20 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0023_customuserlogin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountdetails',
            name='account_number',
            field=models.BigIntegerField(db_index=True, editable=False, help_text='Account Number', unique=True),
        ),
    ]
