# Generated by Django 3.2.3 on 2021-06-17 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clients', '0017_job_posts_short_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientsmodels',
            name='Client_profile',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='job_posts',
            name='logo',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
