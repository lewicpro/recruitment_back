# Generated by Django 3.2.3 on 2021-08-06 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Clients', '0037_remove_voucher_voucher'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='applied',
            options={'verbose_name_plural': 'Applications'},
        ),
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='client_profile',
            options={'verbose_name_plural': 'Client profiles'},
        ),
        migrations.AlterModelOptions(
            name='clientsmodels',
            options={'verbose_name_plural': 'List of clients'},
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name_plural': 'Companies'},
        ),
        migrations.AlterModelOptions(
            name='cv',
            options={'verbose_name_plural': 'List of CV'},
        ),
        migrations.AlterModelOptions(
            name='deleted',
            options={'verbose_name_plural': 'Deleted info'},
        ),
        migrations.AlterModelOptions(
            name='experiencemodels',
            options={'verbose_name_plural': 'Experience'},
        ),
        migrations.AlterModelOptions(
            name='job_posts',
            options={'verbose_name_plural': 'Job Posts'},
        ),
        migrations.AlterModelOptions(
            name='job_requests',
            options={'verbose_name_plural': 'Jobs'},
        ),
        migrations.AlterModelOptions(
            name='qualificationmodels',
            options={'verbose_name_plural': 'Qualifications'},
        ),
        migrations.AlterModelOptions(
            name='skillsmodels',
            options={'verbose_name_plural': 'Skills'},
        ),
        migrations.AlterModelOptions(
            name='voucher',
            options={'verbose_name_plural': 'Create voucher'},
        ),
    ]
