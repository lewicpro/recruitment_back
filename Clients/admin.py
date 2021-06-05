from django.contrib import admin
from .models import *

# Register your models here.
class Job_RequestsAdmin(admin.ModelAdmin):
    search_fields = ('client_first_name', 'client_third_name', 'Mobile_number', 'Age', 'City', 'Job_seeking'
            )
    list_display=['client_first_name', 'client_third_name', 'Mobile_number', 'Age', 'City', 'Job_seeking']

class Job_PostsAdmin(admin.ModelAdmin):
    search_fields = ('Qualification', 'officer', 'category', 'title', 'start', 'description', 'end',
            )
    list_display=['Qualification', 'officer', 'title', 'start', 'description', 'end',]

class QualificationAdmin(admin.ModelAdmin):
    search_fields = ('user', 'company', 'fromeducation', 'Qualification', 'toeducation', 'university_education',
            )
    list_display=['user', 'company', 'fromeducation', 'Qualification', 'toeducation', 'university_education',]
class AppliedAdmin(admin.ModelAdmin):
    search_fields = ('Date_applied', 'Job_title', 'applicant_username',  'name_of_applicant', 'Age_of_applicant', 'company', 'category', 'officer_posted', 'description', 'start', 'end', 'title', 'start',
            )
    list_display=['Date_applied', 'Job_title', 'applicant_username',  'name_of_applicant', 'Age_of_applicant', 'company', 'category', 'officer_posted', 'description', 'start', 'end', 'title', 'start',]
class DeletedAdmin(admin.ModelAdmin):
    search_fields = ('pk', 'Date_deleted', 'Section', 'Person_deleted',  'Heading_thread', 'company', 'officer',
            )
    list_display=['pk', 'Date_deleted', 'Section', 'Person_deleted',  'Heading_thread', 'company', 'officer',]

class SkillsAdmin(admin.ModelAdmin):
    search_fields = ('user', 'company', 'fromskill', 'toskill', 'company_attended',
            )
    list_display=['user', 'company', 'fromskill', 'toskill', 'company_attended',]

class CVAdmin(admin.ModelAdmin):
    search_fields = ('dateaded', 'fullname',  'company', 'cvtittle', 'cvfile', 'status',
            )
    list_display=['dateaded', 'fullname',  'company', 'cvtittle', 'cvfile', 'status']

class ClientsAdmin(admin.ModelAdmin):
    search_fields = ['username', 'fullname',  'position', 'description', 'end', 'client_second_name', 'Country_code', 'Client_profile', 'Mobile_number', 'Complete_address', 'Nationality', 'upload_cv', 'Age', 'faceboo_url', 'spark_url', 'pinterest_url', ]
            
    list_display=['username', 'fullname',  'position', 'description', 'end', 'client_second_name', 'Country_code', 'Client_profile', 'Mobile_number', 'Complete_address', 'Nationality', 'upload_cv', 'Age', 'faceboo_url', 'spark_url', 'pinterest_url',]
class ExperienceAdmin(admin.ModelAdmin):
    search_fields = ['user', 'company', 'skillsexperience', 'Levelexperience', 'status', ]
            
    list_display=['user', 'company', 'skillsexperience', 'Levelexperience', 'status',]


class PackagesAdmin(admin.ModelAdmin):
    search_fields = ['dateaded', 'package', 'company', 'timeframe', 'fullname', 'percentage', 'status', ]
            
    list_display=('dateaded', 'package', 'company', 'timeframe', 'fullname', 'percentage', 'status', )

admin.site.register(Job_requests, Job_RequestsAdmin)
admin.site.register(Job_Posts, Job_PostsAdmin)
admin.site.register(ClientsModels, ClientsAdmin)
admin.site.register(QualificationModels, QualificationAdmin)
admin.site.register(SkillsModels, SkillsAdmin)
admin.site.register(ExperienceModels, ExperienceAdmin)
admin.site.register(CV, CVAdmin)
admin.site.register(Packages, PackagesAdmin)
admin.site.register(Applied, AppliedAdmin)
admin.site.register(Deleted, DeletedAdmin)