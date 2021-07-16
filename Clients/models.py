from django.db import models
from django.contrib.auth.models import User
import random, string


class Job_requests(models.Model):
    client_first_name=models.CharField(max_length=120, blank=True, null=True)
    client_second_name=models.CharField(max_length=120, blank=True, null=True)
    client_third_name=models.CharField(max_length=120, blank=True, null=True)
    Country_code=models.CharField(max_length=120, blank=True, null=True)
    Birthdate=models.CharField(max_length=120, blank=True, null=True)
    Client_profile=models.CharField(max_length=120, blank=True, null=True)
    Email=models.CharField(max_length=120, blank=True, null=True)
    Mobile_number=models.CharField(max_length=120, blank=True, null=True)
    Gender=models.CharField(max_length=120, blank=True, null=True)
    Complete_address=models.CharField(max_length=120, blank=True, null=True)
    Age=models.CharField(max_length=120, blank=True, null=True)
    Nationality=models.CharField(max_length=120, blank=True, null=True)
    City=models.CharField(max_length=120, blank=True, null=True)
    upload_cv=models.CharField(max_length=120, blank=True, null=True)
    category=models.CharField(max_length=120, blank=True, null=True)
    # Age=models.CharField(max_length=120, blank=True, null=True)
    Job_seeking=models.CharField(max_length=120, blank=True, null=True)
    faceboo_url=models.CharField(max_length=120, blank=True, null=True)
    instagram_url=models.CharField(max_length=120, blank=True, null=True)
    spark_url=models.CharField(max_length=120, blank=True, null=True)
    twitter_url=models.CharField(max_length=120, blank=True, null=True)
    pinterest_url=models.CharField(max_length=120, blank=True, null=True)

class Job_Posts(models.Model):
    Qualification=models.CharField(max_length=120, blank=True, null=True)
    company=models.CharField(max_length=120, blank=True, null=True)
    workexperience=models.CharField(max_length=120, blank=True, null=True)
    experience=models.CharField(max_length=120, blank=True, null=True)
    category=models.CharField(max_length=120, blank=True, null=True)
    officer=models.CharField(max_length=120, blank=True, null=True)
    title=models.CharField(max_length=120, blank=True, null=True)
    description=models.CharField(max_length=120, blank=True, null=True)
    start=models.CharField(max_length=120, blank=True, null=True)
    location=models.CharField(max_length=120, blank=True, null=True)
    Gender=models.CharField(max_length=120, blank=True, null=True)
    language=models.CharField(max_length=120, blank=True, null=True)
    working_type=models.CharField(max_length=120, blank=True, null=True)
    Short_description=models.CharField(max_length=30, blank=True, null=True)
    end=models.CharField(max_length=120, blank=True, null=True)
    logo=models.FileField(blank=True)

class categories(models.Model):
    date=models.DateField()
    user=models.CharField(max_length=120, blank=True, null=True)
    company=models.CharField(max_length=120, blank=True, null=True)
    category=models.CharField(max_length=120, blank=True, null=True)

class Applied(models.Model):
    Date_applied=models.CharField(max_length=120, blank=True, null=True)
    Job_title=models.CharField(max_length=120, blank=True, null=True)
    Qualification=models.CharField(max_length=120, blank=True, null=True)
    applicant_username=models.CharField(max_length=120, blank=True, null=True)
    name_of_applicant=models.CharField(max_length=120, blank=True, null=True)
    Age_of_applicant=models.CharField(max_length=120, blank=True, null=True)
    company=models.CharField(max_length=120, blank=True, null=True)
    Gender=models.CharField(max_length=120, blank=True, null=True)
    location=models.CharField(max_length=120, blank=True, null=True)
    category=models.CharField(max_length=120, blank=True, null=True)
    officer_posted=models.CharField(max_length=120, blank=True, null=True)
    status=models.CharField(max_length=120, blank=True, default="pending")
    start=models.CharField(max_length=120, blank=True, null=True)
    end=models.CharField(max_length=120, blank=True, null=True)
    title=models.CharField(max_length=120, blank=True, null=True)
    description=models.CharField(max_length=120, blank=True, null=True)
    workexperience=models.CharField(max_length=120, blank=True, null=True)
    experience=models.CharField(max_length=120, blank=True, null=True)
    end=models.CharField(max_length=120, blank=True, null=True)

class Deleted(models.Model):
    Date_deleted=models.CharField(max_length=120, blank=True, null=True)
    Section=models.CharField(max_length=120, blank=True, null=True)
    Person_deleted=models.CharField(max_length=120, blank=True, null=True)
    Heading_thread=models.CharField(max_length=120, blank=True, null=True)
    company=models.CharField(max_length=120, blank=True, null=True)
    officer=models.CharField(max_length=120, blank=True, null=True)



class ClientsModels(models.Model):
    username=models.CharField(max_length=120, blank=True, null=True)
    email=models.CharField(max_length=120, blank=True, null=True)
    fullname=models.CharField(max_length=120, blank=True, null=True)
    password=models.CharField(max_length=120, blank=True, null=True)
    description=models.CharField(max_length=120, blank=True, null=True)
    start=models.CharField(max_length=120, blank=True, null=True)
    end=models.CharField(max_length=120, blank=True, null=True)
    client_first_name=models.CharField(max_length=120, blank=True, null=True)
    client_second_name=models.CharField(max_length=120, blank=True, null=True)
    client_third_name=models.CharField(max_length=120, blank=True, null=True)
    Country_code=models.CharField(max_length=120, blank=True, null=True)
    Birthdate=models.CharField(max_length=120, blank=True, null=True)
    Client_profile=models.FileField(blank=True, null=True)
    # Email=models.CharField(max_length=120, blank=True, null=True)
    Mobile_number=models.CharField(max_length=120, blank=True, null=True)
    Gender=models.CharField(max_length=120, blank=True, null=True)
    Country=models.CharField(max_length=120, blank=True, null=True)
    Complete_address=models.CharField(max_length=120, blank=True, null=True)
    Age=models.CharField(max_length=120, blank=True, null=True)
    Nationality=models.CharField(max_length=120, blank=True, null=True)
    position=models.CharField(max_length=120, blank=True, null=True)
    City=models.CharField(max_length=120, blank=True, null=True)
    upload_cv=models.CharField(max_length=120, blank=True, null=True)
    category=models.CharField(max_length=120, blank=True, null=True)
    company=models.CharField(max_length=120, blank=True, default='self')
    Job_seeking=models.CharField(max_length=120, blank=True, null=True)
    faceboo_url=models.CharField(max_length=120, blank=True, null=True)
    instagram_url=models.CharField(max_length=120, blank=True, null=True)
    spark_url=models.CharField(max_length=120, blank=True, null=True)
    Linkedin=models.CharField(max_length=120, blank=True, null=True)
    twitter_url=models.CharField(max_length=120, blank=True, null=True)
    pinterest_url=models.CharField(max_length=120, blank=True, null=True)
    company_profile=models.CharField(max_length=120, blank=True, null=True)
    logo=models.FileField(blank=True, null=True)


class QualificationModels(models.Model):
    user = models.CharField(max_length=120, null=True)
    company=models.CharField(max_length=120, blank=True, null=True)
    Qualification=models.CharField(max_length=120, blank=True, null=True)
    fromeducation=models.CharField(max_length=120, blank=True, null=True)
    toeducation=models.CharField(max_length=120, blank=True, null=True)
    university_education=models.CharField(max_length=120, blank=True, null=True)
    toeducation=models.CharField(max_length=120, blank=True, null=True)

    
class SkillsModels(models.Model):
    user = models.CharField(max_length=120, null=True)
    company=models.CharField(max_length=120, blank=True, null=True)
    skill=models.CharField(max_length=120, blank=True, null=True)
    fromskill=models.CharField(max_length=120, blank=True, null=True)
    toskill=models.CharField(max_length=120, blank=True, null=True)
    company_attended=models.CharField(max_length=120, blank=True, null=True)
    status=models.CharField(max_length=120, blank=True, null=True)

    
class ExperienceModels(models.Model):
    user = models.CharField(max_length=120, null=True)
    company=models.CharField(max_length=120, blank=True, null=True)
    skillsexperience=models.CharField(max_length=120, blank=True, null=True)
    Levelexperience=models.CharField(max_length=120, blank=True, null=True)
    status=models.CharField(max_length=120, blank=True, null=True)

    
class CV(models.Model):
    dateaded=models.CharField(max_length=120, blank=True, null=True)
    user = models.CharField(max_length=120, null=True)
    company=models.CharField(max_length=120, blank=True, null=True)
    fullname=models.CharField(max_length=120, blank=True, null=True)
    cvtittle=models.CharField(max_length=120, blank=True, null=True)
    cvfile=models.FileField(blank=True, null=True)
    status=models.CharField(max_length=120, blank=True, default='Active')

    

    
class Packages(models.Model):
    dateaded=models.CharField(max_length=120, blank=True, null=True)
    user = models.CharField(max_length=120, null=True)
    package=models.CharField(max_length=120, blank=True, null=True)
    company=models.CharField(max_length=120, blank=True, null=True)
    fullname=models.CharField(max_length=120, blank=True, null=True)
    timeframe=models.CharField(max_length=120, blank=True, null=True)
    percentage=models.CharField(max_length=120, blank=True, null=True)
    Description=models.CharField(max_length=120, blank=True, default='Active')
    status=models.CharField(max_length=120, blank=True, default='Active')

    
class Company(models.Model):
    date_added=models.DateTimeField(max_length=120, blank=True, null=True)
    company_name =models.CharField(max_length=120, blank=True, null=True)
    officer_added = models.CharField(max_length=120, blank=True, null=True)
    profile_photo =models.CharField(max_length=120, blank=True, null=True)
    bio =models.CharField(max_length=120, blank=True, null=True)

class Client_profile(models.Model):
    date_added=models.DateTimeField(auto_now=True, auto_now_add=False, null=True)
    username =models.CharField(max_length=120, blank=True, null=True)
    company_name =models.CharField(max_length=120, blank=True, null=True)
    officer_name = models.CharField(max_length=120, blank=True, null=True)
    possition = models.CharField(max_length=120, blank=True, null=True)
    profile_photo =models.FileField(blank=True, null=True)
    bio=models.CharField(max_length=120, blank=True, null=True)


used = 'used'
new = 'new'
sign = (
    (new, 'new'),
    (used, 'used'),
)
class Voucher(models.Model):
    voucher_token=models.CharField(max_length=120, unique=True, blank=True, null=True)
    username =models.CharField(max_length=120, blank=True, null=True)
    company_name =models.CharField(max_length=120, blank=True, null=True)
    status =models.CharField(max_length=120, blank=True, null=True, choices=sign)

    def save(self, *args, **kwargs):
        if self.voucher_token is None or self.voucher_token == "":
            self.voucher_token = account_generator()
        super(Voucher, self).save(*args, **kwargs)

    

def account_generator(size=8, chars=string.digits):
    account = 'http://localhost:4200/regcompany/?token=SPK' + ''
    for _ in range(size):
        account += random.choice(chars)
    return account