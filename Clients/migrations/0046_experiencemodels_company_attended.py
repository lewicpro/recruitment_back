# Generated by Django 3.2.3 on 2021-09-12 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clients', '0045_auto_20210912_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiencemodels',
            name='company_attended',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]