# Generated by Django 5.0 on 2024-09-19 08:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerPersonalInfo',
            fields=[
                ('index', models.BigAutoField(db_index=True, primary_key=True, serialize=False)),
                ('title', models.CharField(choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Ms', 'Ms')], max_length=3, verbose_name='Title')),
                ('first_name', models.CharField(max_length=10, verbose_name='First Name')),
                ('middle_name', models.CharField(blank=True, max_length=10, verbose_name='Middle Name')),
                ('last_name', models.CharField(max_length=10, verbose_name='Last Name')),
                ('dob', models.DateField(verbose_name='Date of Birth')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=6, verbose_name='Gender')),
                ('pan', models.CharField(max_length=15, unique=True, verbose_name='PAN')),
                ('aadhaar', models.CharField(max_length=12, unique=True, verbose_name='Aadhaar Card')),
                ('occupation', models.CharField(choices=[('Student', 'Student'), ('Salaried', 'Salaried'), ('Non-Salaried', 'Non-Salaried'), ('Housewife', 'Housewife'), ('Other', 'Other')], max_length=13, verbose_name='Occupation')),
                ('annual_income', models.IntegerField(verbose_name='Annual Income')),
                ('nationality', models.CharField(max_length=19, verbose_name='Nationality')),
                ('account_opening_date_time', models.DateTimeField(auto_now_add=True)),
                ('account_type', models.CharField(choices=[('Saving BANK ACCOUNT', 'Saving BANK ACCOUNT'), ('Current BANK ACCOUNT', 'Current BANK ACCOUNT')], max_length=22, verbose_name='Account Type')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('contact_type', models.CharField(max_length=20, verbose_name='Contact Type')),
                ('contact', models.BigIntegerField(verbose_name='Contact')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('cust', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.customerpersonalinfo', verbose_name='Customer')),
            ],
        ),
        migrations.CreateModel(
            name='AddressInfo',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('address_type', models.CharField(max_length=20, verbose_name='Address Type')),
                ('house_no', models.CharField(max_length=5, verbose_name='House No')),
                ('street', models.CharField(max_length=20, verbose_name='Street')),
                ('city', models.CharField(max_length=20, verbose_name='City')),
                ('state', models.CharField(max_length=20, verbose_name='State')),
                ('country', models.CharField(max_length=20, verbose_name='Country')),
                ('pincode', models.IntegerField(verbose_name='Pincode')),
                ('cust', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.customerpersonalinfo', verbose_name='Customer')),
            ],
        ),
        migrations.CreateModel(
            name='SecurityQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(choices=[('mother_maiden_name', "What is your mother's maiden name?"), ('first_pet', 'What was the name of your first pet?')], max_length=50, verbose_name='Security Question')),
                ('answer', models.CharField(max_length=100, verbose_name='Answer')),
                ('cust', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='index.customerpersonalinfo', verbose_name='Customer')),
            ],
        ),
    ]