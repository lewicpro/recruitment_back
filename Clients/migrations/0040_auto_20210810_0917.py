# Generated by Django 3.2.3 on 2021-08-10 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clients', '0039_auto_20210808_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applied',
            name='Qualification',
            field=models.TextField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='applied',
            name='description',
            field=models.TextField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='clientsmodels',
            name='description',
            field=models.TextField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='job_posts',
            name='Qualification',
            field=models.TextField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='job_posts',
            name='description',
            field=models.TextField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='packages',
            name='Description',
            field=models.TextField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='qualificationmodels',
            name='Qualification',
            field=models.TextField(blank=True, default=True),
        ),
    ]
