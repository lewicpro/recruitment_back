# Generated by Django 3.2.3 on 2021-06-02 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clients', '0014_clientsmodels_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientsmodels',
            name='Linkedin',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
