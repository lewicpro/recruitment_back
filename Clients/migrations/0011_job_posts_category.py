# Generated by Django 3.2.3 on 2021-05-28 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clients', '0010_alter_packages_percentage'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_posts',
            name='category',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
