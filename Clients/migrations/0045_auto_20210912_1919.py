# Generated by Django 3.2.3 on 2021-09-12 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clients', '0044_alter_emails_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiencemodels',
            name='from_date',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='experiencemodels',
            name='role',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='experiencemodels',
            name='to_date',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]