# Generated by Django 5.1.7 on 2025-03-09 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0019_accountdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addressinfo',
            name='pincode',
            field=models.IntegerField(blank=True, max_length=6, null=True, verbose_name='Pincode'),
        ),
        migrations.AlterField(
            model_name='customerpersonalinfo',
            name='annual_income',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Annual Income'),
        ),
    ]
