# Generated by Django 5.1.7 on 2025-03-11 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nomminee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nominee',
            name='contact',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Contact Number'),
        ),
        migrations.AlterField(
            model_name='nominee',
            name='name',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='nominee',
            name='relation',
            field=models.CharField(blank=True, max_length=18, verbose_name='Relation'),
        ),
    ]
