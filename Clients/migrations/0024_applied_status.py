# Generated by Django 3.2.3 on 2021-06-23 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clients', '0023_clientsmodels_company_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='applied',
            name='status',
            field=models.CharField(blank=True, default='pending', max_length=120),
        ),
    ]