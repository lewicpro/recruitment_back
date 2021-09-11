from django.contrib import admin
from .models import *


# Register your models here.
class Job_RequestsAdmin(admin.ModelAdmin):
    search_fields = ('client_first_name', 'client_third_name', 'Mobile_number', 'Age', 'City', 'Job_seeking'
            )
    list_display=['client_first_name', 'client_third_name', 'Mobile_number', 'Age', 'City', 'Job_seeking']

class Job_PostsAdmin(admin.ModelAdmin):
    search_fields = ('Qualification', 'officer', 'location', 'working_type', 'category', 'title', 'start', 'description', 'end',
            )
    list_display=['Qualification', 'officer', 'location', 'working_type', 'title', 'start', 'description', 'end',]

class QualificationAdmin(admin.ModelAdmin):
    search_fields = ('user', 'company', 'fromeducation', 'Qualification', 'toeducation', 'university_education',
            )
    list_display=['user', 'company', 'fromeducation', 'Qualification', 'toeducation', 'university_education',]
    readonly_fields = ('company', )   
class ClientProfileAdmin(admin.ModelAdmin):
    search_fields = ('date_added', 'username', 'company_name', 'officer_name', 'possition', 'profile_photo', 'bio',)
    list_display=['date_added', 'username', 'company_name', 'officer_name', 'possition', 'profile_photo', 'bio',]
    list_filter = ('username',)
class CompanyProfileAdmin(admin.ModelAdmin):
    search_fields = ( 'company_name', 'officer_added', 'profile_photo', 'bio',
            )
    list_display=['company_name', 'officer_added', 'profile_photo', 'bio',]
    def officer_added(self, obj):
        return obj.get_full_name()
    officer_added.short_description = 'Date adde'
    
class AppliedAdmin(admin.ModelAdmin):
    search_fields = ('Date_applied', 'Job_title', 'applicant_username',  'name_of_applicant', 'company', 'category', 'officer_posted', 'description', 'start', 'end', 'title',
            )
    list_display=['Date_applied', 'Job_title', 'applicant_username',  'name_of_applicant', 'company', 'category', 'short_description', 'start', 'end', 'title',]
    # short_description=['description']
class DeletedAdmin(admin.ModelAdmin):
    search_fields = ('pk', 'Date_deleted', 'Section', 'Person_deleted',  'Heading_thread', 'company', 'officer',
            )
    list_display=['pk', 'Date_deleted', 'Section', 'Person_deleted',  'Heading_thread', 'company', 'officer',]

class SkillsAdmin(admin.ModelAdmin):
    search_fields = ('user', 'company', 'fromskill', 'toskill', 'company_attended',
            )
    list_display=['user', 'company', 'fromskill', 'toskill', 'company_attended',]
    readonly_fields = ('company', )   
class VoucherAdmin(admin.ModelAdmin):
    search_fields = ('voucher_token', 'username', 'company_name',)
    list_display=['voucher_token', 'username', 'company_name', 'status',]
class EmailsAdmin(admin.ModelAdmin):
    search_fields = ('email', 'date', 'user','content', 'subject',)
    list_display=['email', 'date', 'user','content', 'subject',]


class categoriesAdmin(admin.ModelAdmin):
    search_fields = ('date', 'user', 'company', 'category',)
    list_display=['date', 'user', 'company', 'category',]
    readonly_fields = ('company', )   

class CVAdmin(admin.ModelAdmin):
    search_fields = ('dateaded', 'fullname',  'company', 'cvtittle', 'cvfile', 'status',
            )
    list_display=['dateaded', 'fullname',  'company', 'cvtittle', 'cvfile', 'status']
    readonly_fields = ('company', )   

class ClientsAdmin(admin.ModelAdmin):
    search_fields = ['username', 'fullname', 'token', 'position', 'company', 'description', 'end', 'client_second_name', 'Country_code', 'Client_profile', 'Mobile_number', 'Complete_address', 'Nationality', 'upload_cv', 'Age', 'faceboo_url', 'spark_url', 'pinterest_url', ]
            
    list_display=['username', 'fullname', 'token',  'position', 'company', 'description', 'end', 'client_second_name', 'Country_code', 'Client_profile', 'Mobile_number', 'Complete_address', 'Nationality', 'upload_cv', 'Age', 'faceboo_url', 'spark_url', 'pinterest_url',]
    readonly_fields = ('company', )
    list_filter = ('position',)
class ExperienceAdmin(admin.ModelAdmin):
    search_fields = ['user', 'company', 'skillsexperience', 'Levelexperience', 'status', ]
            
    list_display=['user', 'company', 'skillsexperience', 'Levelexperience', 'status',]
    readonly_fields = ('company', )   


class PackagesAdmin(admin.ModelAdmin):
    search_fields = ['dateaded', 'package', 'company', 'timeframe', 'fullname', 'percentage', 'status', ]
            
    list_display=('dateaded', 'package', 'company', 'timeframe', 'fullname', 'percentage', 'status', )
    readonly_fields = ('company', )   

# admin.site.register(Job_requests, Job_RequestsAdmin)
admin.site.register(Job_Posts, Job_PostsAdmin)
admin.site.register(ClientsModels, ClientsAdmin)
admin.site.register(QualificationModels, QualificationAdmin)
admin.site.register(SkillsModels, SkillsAdmin)
admin.site.register(ExperienceModels, ExperienceAdmin)
admin.site.register(CV, CVAdmin)
admin.site.register(Packages, PackagesAdmin)
admin.site.register(categories, categoriesAdmin)
admin.site.register(Voucher, VoucherAdmin)
admin.site.register(Applied, AppliedAdmin)
# admin.site.register(Deleted, DeletedAdmin)
admin.site.register(Client_profile, ClientProfileAdmin)
admin.site.register(Company, CompanyProfileAdmin)
admin.site.register(Emails, EmailsAdmin)
