# Generated by Django 5.1.7 on 2025-03-08 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0005_alter_emailpreferences_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='isauthenticated',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
