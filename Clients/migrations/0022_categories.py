# Generated by Django 3.2.3 on 2021-06-22 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clients', '0021_auto_20210620_0912'),
    ]

    operations = [
        migrations.CreateModel(
            name='categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('user', models.CharField(blank=True, max_length=120, null=True)),
                ('company', models.CharField(blank=True, max_length=120, null=True)),
                ('category', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
    ]
