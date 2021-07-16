# Generated by Django 3.2.3 on 2021-06-25 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clients', '0026_client_profile_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client_profile',
            name='date_added',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='date_added',
            field=models.DateTimeField(blank=True, max_length=120, null=True),
        ),
    ]