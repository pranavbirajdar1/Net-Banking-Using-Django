# Generated by Django 5.0 on 2025-01-23 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_newsletter_date_subscribed'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NewsLetter',
        ),
    ]
