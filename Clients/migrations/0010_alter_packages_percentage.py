# Generated by Django 3.2.3 on 2021-05-26 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clients', '0009_packages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packages',
            name='percentage',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
