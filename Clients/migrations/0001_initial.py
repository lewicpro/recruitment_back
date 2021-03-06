# Generated by Django 3.2.3 on 2021-05-23 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientsModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=120, null=True)),
                ('email', models.CharField(blank=True, max_length=120, null=True)),
                ('fullname', models.CharField(blank=True, max_length=120, null=True)),
                ('password', models.CharField(blank=True, max_length=120, null=True)),
                ('description', models.CharField(blank=True, max_length=120, null=True)),
                ('start', models.CharField(blank=True, max_length=120, null=True)),
                ('end', models.CharField(blank=True, max_length=120, null=True)),
                ('client_first_name', models.CharField(blank=True, max_length=120, null=True)),
                ('client_second_name', models.CharField(blank=True, max_length=120, null=True)),
                ('client_third_name', models.CharField(blank=True, max_length=120, null=True)),
                ('Country_code', models.CharField(blank=True, max_length=120, null=True)),
                ('Birthdate', models.CharField(blank=True, max_length=120, null=True)),
                ('Client_profile', models.CharField(blank=True, max_length=120, null=True)),
                ('Mobile_number', models.CharField(blank=True, max_length=120, null=True)),
                ('Gender', models.CharField(blank=True, max_length=120, null=True)),
                ('Complete_address', models.CharField(blank=True, max_length=120, null=True)),
                ('Age', models.CharField(blank=True, max_length=120, null=True)),
                ('Nationality', models.CharField(blank=True, max_length=120, null=True)),
                ('position', models.CharField(blank=True, max_length=120, null=True)),
                ('City', models.CharField(blank=True, max_length=120, null=True)),
                ('upload_cv', models.CharField(blank=True, max_length=120, null=True)),
                ('category', models.CharField(blank=True, max_length=120, null=True)),
                ('Job_seeking', models.CharField(blank=True, max_length=120, null=True)),
                ('faceboo_url', models.CharField(blank=True, max_length=120, null=True)),
                ('instagram_url', models.CharField(blank=True, max_length=120, null=True)),
                ('spark_url', models.CharField(blank=True, max_length=120, null=True)),
                ('twitter_url', models.CharField(blank=True, max_length=120, null=True)),
                ('pinterest_url', models.CharField(blank=True, max_length=120, null=True)),
                ('logo', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Job_Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Qualification', models.CharField(blank=True, max_length=120, null=True)),
                ('company', models.CharField(blank=True, max_length=120, null=True)),
                ('officer', models.CharField(blank=True, max_length=120, null=True)),
                ('title', models.CharField(blank=True, max_length=120, null=True)),
                ('description', models.CharField(blank=True, max_length=120, null=True)),
                ('start', models.CharField(blank=True, max_length=120, null=True)),
                ('end', models.CharField(blank=True, max_length=120, null=True)),
                ('logo', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Job_requests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_first_name', models.CharField(blank=True, max_length=120, null=True)),
                ('client_second_name', models.CharField(blank=True, max_length=120, null=True)),
                ('client_third_name', models.CharField(blank=True, max_length=120, null=True)),
                ('Country_code', models.CharField(blank=True, max_length=120, null=True)),
                ('Birthdate', models.CharField(blank=True, max_length=120, null=True)),
                ('Client_profile', models.CharField(blank=True, max_length=120, null=True)),
                ('Email', models.CharField(blank=True, max_length=120, null=True)),
                ('Mobile_number', models.CharField(blank=True, max_length=120, null=True)),
                ('Gender', models.CharField(blank=True, max_length=120, null=True)),
                ('Complete_address', models.CharField(blank=True, max_length=120, null=True)),
                ('Age', models.CharField(blank=True, max_length=120, null=True)),
                ('Nationality', models.CharField(blank=True, max_length=120, null=True)),
                ('City', models.CharField(blank=True, max_length=120, null=True)),
                ('upload_cv', models.CharField(blank=True, max_length=120, null=True)),
                ('category', models.CharField(blank=True, max_length=120, null=True)),
                ('Job_seeking', models.CharField(blank=True, max_length=120, null=True)),
                ('faceboo_url', models.CharField(blank=True, max_length=120, null=True)),
                ('instagram_url', models.CharField(blank=True, max_length=120, null=True)),
                ('spark_url', models.CharField(blank=True, max_length=120, null=True)),
                ('twitter_url', models.CharField(blank=True, max_length=120, null=True)),
                ('pinterest_url', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
    ]
