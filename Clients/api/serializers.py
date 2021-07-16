from rest_framework import serializers
from ..models import *
from django.contrib.auth import get_user_model
from rest_framework.serializers import CharField, EmailField, ValidationError, SerializerMethodField
from django.db.models import Q
User = get_user_model()







class UserLoginSerializer(serializers.ModelSerializer):
    # token = CharField(allow_blank=True, read_only=True)
    username = CharField(allow_blank=True)
    # email = EmailField(label="email ", allow_blank=True)
    
    class Meta:
        model = User
        fields =[
            'pk', 
            'username',
            # 'email',
            'password',
            # 'token',
        ]

        extra_kwargs = {"password":
                                {"write_only": True}
                                }

    def validate(self, data):
        user_obj =None
        email = data.get("email", None)
        username = data.get("username", None)
        password = data["password"]
        if not email and not username:
            raise ValidationError("A username or Email is required to login")

        user =User.objects.filter(
            Q(email=email) |
            Q(username=username)
            ).distinct()
        user = user.exclude(email__isnull=True).exclude(email__iexact='')
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("This username/email is not valid.")
        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect password")
        data["token"] = "SOME RANDOM TO"


        return data






# class authSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = authdataModel
#         fields=[
#             'pk',
#             'user',
#             'datavalue',
#         ]

class Job_requestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job_requests
        fields=[
            'pk', 'client_first_name', 'client_second_name', 'client_third_name', 'Birthdate', 'Nationality', 'Complete_address', 'Mobile_number', 'Email', 'Gender', 'Age', 'City', 'Age', 'faceboo_url', 'instagram_url', 'spark_url', 'twitter_url', 'pinterest_url',
        ]

class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualificationModels
        fields=['pk', 'user', 'company', 'fromeducation', 'Qualification', 'toeducation', 'university_education',]

class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillsModels
        fields=['pk', 'user', 'company', 'fromskill', 'skill', 'toskill', 'company_attended',]
class  ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceModels
        fields=['pk', 'user', 'company', 'skillsexperience', 'Levelexperience', 'status',]

class  CVSerializer(serializers.ModelSerializer):
    class Meta:
        model = CV
        fields=['pk', 'dateaded', 'user', 'fullname',  'company', 'cvtittle', 'cvfile', 'status']

class  CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = categories
        fields=['date', 'user', 'company', 'category',]

class  PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packages
        fields=['pk', 'dateaded', 'user', 'package', 'company', 'timeframe', 'fullname', 'percentage', 'status', ]

class Job_PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job_Posts
        fields=[
            'pk', 
            'Qualification', 
            'workexperience', 
            'experience', 
            'company', 
            'Gender', 
            'language', 
            'officer', 
            'category', 
            'title', 
            'start', 
            'description', 
            'end',
            'location', 
            'working_type',
            'Short_description',
        ]
class ClientProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Client_profile
        fields=[
            'pk', 'date_added', 'username', 'company_name', 'officer_name', 'possition', 'profile_photo', 'bio',
        ]
class CompanyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields=[
            'pk', 'date_added', 'company_name', 'officer_added', 'profile_photo', 'bio',
        ]
class Job_PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job_Posts
        fields=[
            'pk', 
            'Qualification', 
            'workexperience', 
            'experience', 
            'company', 
            'Gender', 
            'language', 
            'officer', 
            'category', 
            'title', 
            'start', 
            'description', 
            'end',
            'location', 
            'working_type',
            'Short_description',
        ]

class ApplyJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applied
        fields=['pk', 'Qualification', 'Date_applied', 'Job_title', 'Gender', 'location', 'applicant_username', 'workexperience', 'experience',  'name_of_applicant', 'Age_of_applicant', 'company', 'category', 'officer_posted', 'description', 'start', 'end', 'title', 'status', 'start',]
        
class DeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deleted
        fields=['pk', 'Date_deleted', 'Section', 'Person_deleted',  'Heading_thread', 'company', 'officer',]
        
class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientsModels
        fields=['pk', 'username', 'Gender', 'fullname', 'company', 'email', 'description', 'end',  'position', 'start', 'company_profile',  'client_first_name', 'client_second_name', 'client_third_name', 'Birthdate', 'Client_profile', 'Mobile_number', 'Complete_address', 'Nationality', 'upload_cv', 'Age', 'twitter_url',  'faceboo_url', 'instagram_url', 'Country_code', 'spark_url', 'pinterest_url', 'City', 'Country'] 
    

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True, label="Confirm pasword")


    def create(self, validated_data):
        user = get_user_model().objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            

        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model =User
        fields = [
            'pk', 
            'username',
            'password',
            'password2',
            'email'
           ]


    def validate_password2(self, value):
        data = self.get_initial()
        password = data.get("password")
        # username = data.get("username", None)
        password2 = value
        if password != password2:
            raise ValidationError('passwords must be the same')
        return value


class ChangePasswordSerializer(serializers.Serializer):
    model = User
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
