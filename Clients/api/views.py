from django.db.models import fields
from django_filters import filterset
from ..models import *
from .serializers import *
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .filters import *

from datetime import datetime, timedelta
from django.utils import timezone
from .pagination import PostLimitOffsetPagination, PostPageNumberPagination
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated

import os
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
import json
from django.conf import settings
from rest_framework.viewsets import ModelViewSet
import django_filters
from django.core.mail import send_mail

class CreateUserView(generics.CreateAPIView):
	model = get_user_model()
	permission_classes = (AllowAny,)
	serializer_class = UserSerializer

# class ClientView(generics.CreateAPIView):
# 	model = get_user_model()
# 	# permission_classes = (AllowAny,)
# 	serializer_class = UserSerializer


class UserLoginAPIView(APIView):
	permission_classes = [AllowAny]
	serializer_class = UserLoginSerializer


	def post(self, request, *args, **kwargs):
		data = request.data
		serializer = UserLoginSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			# usere = serializer.validated_data['email']
			new_data = serializer.data
			return Response(new_data, status=HTTP_200_OK)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class TokenValidatorAPIView(APIView):
	queryset = Voucher.objects.all()
	permission_classes = [AllowAny]
	def get(self, request, format=None):
		passed = self.request.GET.get('token', None)
		giv=Voucher.objects.filter(voucher_token__icontains=passed)
		for m in giv:
			context={
			    'status':m.status
			}
			return Response(context, status=HTTP_200_OK)

	# def post(self, request, *args, **kwargs):
	# 	data = request.data
	# 	serializer = UserLoginSerializer(data=data)
	# 	if serializer.is_valid(raise_exception=True):
	# 		# usere = serializer.validated_data['email']
	# 		new_data = serializer.data
	# 		return Response(new_data, status=HTTP_200_OK)
	# 	return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class ClientView(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = ClientsSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		# giv=Voucher.objects.filter(voucher_token__icontains=passed)
		return ClientsModels.objects.all()
	
	def post(self, request, *args, **kwargs):
		data = request.data
		# username= self.kwargs["username"]
		serializer = ClientsSerializer(data=data)
		if serializer.is_valid(raise_exception=True):

			username = serializer.validated_data['username']
			Nationality = serializer.validated_data['Nationality']
			company_profile = serializer.validated_data['company_profile']
			Complete_address = serializer.validated_data['Complete_address']
			Country = serializer.validated_data['Country']
	

			moxt=ClientsModels.objects.filter(username=username).update(client_first_name=client_first_name, client_second_name=client_second_name, client_third_name=client_third_name, Birthdate=Birthdate, Country_code=Country_code, City=City, Gender=Gender, Complete_address=Complete_address, Nationality=Nationality, company_profile=company_profile, Mobile_number=Mobile_number, Country=Country )
		# username= self.kwargs["username"]
		# serializer = ClientsSerializer(data=data)
		# if serializer.is_valid(raise_exception=True):

		# 	Nationality = serializer.validated_data['Nationality']
		# 	company_profile = serializer.validated_data['company_profile']
		# 	Complete_address = serializer.validated_data['Complete_address']
		# 	Country = serializer.validated_data['Country']
	

		# 	moxt=ClientsModels.objects.filter(username=username).update(client_first_name=client_first_name, client_second_name=client_second_name, client_third_name=client_third_name, Birthdate=Birthdate, Country_code=Country_code, City=City, Gender=Gender, Complete_address=Complete_address, Nationality=Nationality, company_profile=company_profile, Mobile_number=Mobile_number, Country=Country )

			# mon = serializer.save()

			
			return Response(serializer.validated_data)
class ClientView1(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = ClientsSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		# giv=Voucher.objects.filter(voucher_token__icontains=passed)
		return ClientsModels.objects.all()

	def post(self, request, *args, **kwargs):
		data = request.data
		serializer = ClientsSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			token = serializer.validated_data['token']
			company = serializer.validated_data['company']
			username = serializer.validated_data['username']
			fullname = serializer.validated_data['fullname']
			# password = serializer.validated_data['password']
			Nationality = serializer.validated_data['Nationality']
			email = serializer.validated_data['email']
			position = serializer.validated_data['position']
			update= Voucher.objects.filter(voucher_token=token).update(status='used')
			Company.objects.create(company_name=company, officer_added=email)
			ClientsModels.objects.create(position=position, username=username, company=company, Nationality=Nationality, email=email, fullname=fullname)
			return Response(serializer.validated_data)

class ClientViewnormaluser(generics.CreateAPIView, generics.ListAPIView):
        lookup_field = 'pk'
        serializer_class = ClientsSerializer
        permission_classes = [AllowAny]

        def get_queryset(self):
                return ClientsModels.objects.all()

class qualifaicationView(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = QualificationSerializer

	
	permission_classes = [AllowAny]


	def get_queryset(self):
		user=self.kwargs['username']
		return QualificationModels.objects.filter(user=user)

	def post(self, request, *args, **kwargs):
		data = request.data
		serializer = QualificationSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			mon = serializer.save()
			return Response(serializer.validated_data)

	# def perform_create(self, serializer):
	# 	serializer.save(user=self.request.user)

class SkillsView(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = SkillsSerializer

	
	permission_classes = [AllowAny]


	def get_queryset(self):
		user=self.kwargs['username']
		return SkillsModels.objects.filter(user=user)

	def post(self, request, *args, **kwargs):
		data = request.data
		serializer = SkillsSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			mon = serializer.save()
			return Response(serializer.validated_data)

class ExperienceView(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = ExperienceSerializer

	
	permission_classes = [AllowAny]


	def get_queryset(self):
		user=self.kwargs['username']
		return ExperienceModels.objects.filter(user=user)

	def post(self, request, *args, **kwargs):
		data = request.data
		serializer = ExperienceSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			mon = serializer.save()
			return Response(serializer.validated_data)

class Upadateview(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = ClientsSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		user=self.kwargs['pk']
		return ClientsModels.objects.filter(user=user)

	def post(self, request, *args, **kwargs):
		data = request.data
		username= self.kwargs["username"]
		serializer = ClientsSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			client_first_name = serializer.validated_data['client_first_name']
			client_second_name = serializer.validated_data['client_second_name']
			client_third_name = serializer.validated_data['client_third_name']
			Gender = serializer.validated_data['Gender']
			Country_code = serializer.validated_data['Country_code']
			Birthdate = serializer.validated_data['Birthdate']
			Mobile_number = serializer.validated_data['Mobile_number']
			City = serializer.validated_data['City']
			# logo = serializer.validated_data['logo']
			Nationality = serializer.validated_data['Nationality']
			company_profile = serializer.validated_data['company_profile']
			Complete_address = serializer.validated_data['Complete_address']
			Country = serializer.validated_data['Country']
			# pregstration = serializer.validated_data['pregstration']

			moxt=ClientsModels.objects.filter(username=username).update(client_first_name=client_first_name, client_second_name=client_second_name, client_third_name=client_third_name, Birthdate=Birthdate, Country_code=Country_code, City=City, Gender=Gender, Complete_address=Complete_address, Nationality=Nationality, company_profile=company_profile, Mobile_number=Mobile_number, Country=Country )

			# mon = serializer.save()

			
			return Response(serializer.validated_data)

	# def perform_create(self, serializer):
	# 	serializer.save(user=self.request.user)


class Job_requestsView(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = ClientsSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		return Job_requests.objects.all()

	def post(self, request, *args, **kwargs):
		data = request.data
		username=self.kwargs['username']
		serializer = ClientsSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			client_first_name = serializer.validated_data['client_first_name']
			client_second_name = serializer.validated_data['client_second_name']
			client_third_name = serializer.validated_data['client_third_name']
			Birthdate = serializer.validated_data['Birthdate']
			Mobile_number = serializer.validated_data['Mobile_number']
			# Gender = serializer.validated_data['Gender']
			Complete_address = serializer.validated_data['Complete_address']
			Country = serializer.validated_data['Country']
			# Age = serializer.validated_data['Age']
			Nationality = serializer.validated_data['Nationality']
			Gender = serializer.validated_data['Gender']
			City = serializer.validated_data['City']
			instagram_url = serializer.validated_data['instagram_url']
			spark_url = serializer.validated_data['spark_url']
			# Linkedin = serializer.validated_data['Linkedin']
			Country_code = serializer.validated_data['Country_code']
			twitter_url = serializer.validated_data['twitter_url']
			pinterest_url = serializer.validated_data['pinterest_url']
			faceboo_url = serializer.validated_data['faceboo_url']

			moxt=ClientsModels.objects.filter(username=username).update(client_first_name=client_first_name, client_second_name=client_second_name, client_third_name=client_third_name, Country_code=Country_code, Birthdate=Birthdate, Complete_address=Complete_address, Gender=Gender, Nationality=Nationality, City=City, faceboo_url=faceboo_url, instagram_url=instagram_url, spark_url=spark_url, twitter_url=twitter_url, pinterest_url=pinterest_url, Mobile_number=Mobile_number, Country=Country)
			# mon = serializer.save()

			return Response(serializer.validated_data)
	

class UpdatestatusView(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = ApplyJobSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		return Applied.objects.all()

	def post(self, request, *args, **kwargs):
		data = request.data
		username=self.kwargs['username']
		pk=self.kwargs['pk']
		serializer = ApplyJobSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			company = serializer.validated_data['company']
			status = serializer.validated_data['status']
			# pk = serializer.validated_data['pk']
			moxt=Applied.objects.filter(pk=pk).update(status=status)
			# mon = serializer.save()

			return Response(serializer.validated_data)
	

class uploadprofileView(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = ClientsSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		return ClientsModels.objects.all()

	def post(self, request, *args, **kwargs):
		data = request.data
		username=self.kwargs['username']
		serializer = ClientsSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			username = serializer.validated_data['username']
			Client_profile = serializer.validated_data['Client_profile']
		
			# print(contents)
			moxt=ClientsModels.objects.filter(username=username).update(Client_profile=Client_profile)
			return Response(status=204)
	


class packageview(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = PackageSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		return Packages.objects.all()

class CVView(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = CVSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		user=self.kwargs['username']
		return CV.objects.filter(user=user)


	

class Job_PostsView(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = Job_PostsSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		company=self.kwargs['company']
		return Job_Posts.objects.filter(company=company)


class Job_Posts1View(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = Job_PostsSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		# compay=self.kwargs['company']
		return Job_Posts.objects.all()

class JobDetailsview(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = Job_PostsSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		pk=self.kwargs['pk']
		return Job_Posts.objects.filter(pk=pk)


class jobapplictionsView(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = ApplyJobSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		pk=self.kwargs['pk']
		return Applied.objects.filter(pk=pk)

class jobposthomeView(generics.CreateAPIView, generics.ListAPIView):
		lookup_field = 'pk'
		serializer_class = Job_PostsSerializer
		permission_classes = [AllowAny]
		pagination_class = PostPageNumberPagination
	


		def get_queryset(self):
			return Job_Posts.objects.all().order_by('-pk')
class searchjobsView(generics.CreateAPIView, generics.ListAPIView):
		lookup_field = 'pk'
		serializer_class = Job_PostsSerializer
		permission_classes = [AllowAny]
		# pagination_class = PostPageNumberPagination
		


		def get_queryset(self):
			category=self.kwargs['category']
			momo=self.kwargs['momo']
			if category == 'all':
    				return Job_Posts.objects.all().order_by('-pk')
    				
			if momo == 'rigeon':
    				return Job_Posts.objects.filter(location=category).order_by('-pk')
			if momo == 'category':
					return Job_Posts.objects.filter(category=category).order_by('-pk')

class getalljobsView(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = Job_PostsSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		return Job_Posts.objects.all()

class SearchJobview(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = Job_PostsSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		user=self.kwargs['username']
		Search=self.kwargs['values']
		return Job_Posts.objects.filter(category=Search)

class ApplyJobview(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = ApplyJobSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		user=self.kwargs['username']
		return Applied.objects.filter(applicant_username=user)

	def post(self, request, *args, **kwargs):
		data = request.data
		serializer = ApplyJobSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			mon = serializer.save()
			return Response(serializer.validated_data)

class CategoryView(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = CategorySerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		user=self.kwargs['username']
		return categories.objects.all()


class CompanybioView(generics.CreateAPIView, generics.ListAPIView):
    	
	lookup_field = 'pk'
	serializer_class = ClientsSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		user=self.kwargs['username']
		return ClientsModels.objects.filter(username=user)

class AppliedJobview(generics.CreateAPIView, generics.ListAPIView):
    	
	lookup_field = 'pk'
	serializer_class = ApplyJobSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		company=self.kwargs['company']
		return Applied.objects.filter(company=company)
class EmailsView(generics.CreateAPIView, generics.ListAPIView):
    	
	lookup_field = 'pk'
	serializer_class = EmailsSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		return Emails.objects.all()

	def post(self, request, *args, **kwargs):
		data = request.data
		serializer = EmailsSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
    		# subject = 'Withdraw confirmed'
			# message = 'we will be depositing your cash ( %s usd) within 24 hours' % user.m_amount
			email = serializer.validated_data['email']
			from_email = settings.EMAIL_HOST_USER
			to_list = [email]
			print(from_email)
			print(to_list)
			send_mail('Sent from Spark', 'Welcome to the Spark recruitment portal', from_email, to_list, fail_silently=True)
			mon = serializer.save()
			return Response(serializer.validated_data)
    	
    		

			
			

class CompanyProfileView(generics.CreateAPIView, generics.ListAPIView):
    	
	lookup_field = 'pk'
	serializer_class = CompanyProfileSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		company=self.kwargs['company']
		return Company.objects.filter(company=company)
			
class ClientProfileView(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class =ClientProfileSerializers
	permission_classes = [AllowAny]


	def get_queryset(self):
		username=self.kwargs['username']
		return Client_profile.objects.filter(username=username)



class Deleteview(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = DeleteSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		user=self.kwargs['username']
		return Deleted.objects.filter(applicant_username=user)

	def post(self, request, *args, **kwargs):
		action=self.kwargs['action']
		pks=self.kwargs['pk']
		data = request.data
		serializer = DeleteSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			mon = serializer.save()
			if action=='applied':
				mboma= Applied.objects.get(pk=pks)
				mboma.delete()
			if action=='addedu':
				mboma= QualificationModels.objects.get(pk=pks)
				mboma.delete()
			if action=='skills':
				mboma= SkillsModels.objects.get(pk=pks)
				mboma.delete()
			if action=='expertise':
				mboma= ExperienceModels.objects.get(pk=pks)
				mboma.delete()
			if action=='postjob':
				mboma= Job_Posts.objects.get(pk=pks)
				mboma.delete()
			if action=='Certificate':
				mboma= CV.objects.get(pk=pks)
				mboma.delete()
			

			return Response(serializer.validated_data)


# class authdataModelView(generics.RetrieveUpdateDestroyAPIView, generics.CreateAPIView, generics.ListAPIView):
# 	lookup_field = 'pk'
# 	serializer_class = authSerializer
# 	# permission_classes = [AllowAny]


# 	def get_queryset(self):
# 		return authdataModel.objects.all()



# class nameslView( generics.CreateAPIView, generics.ListAPIView):
# 	lookup_field = 'pk'
# 	serializer_class = NamesSerializer
# 	# permission_classes = [AllowAny]


# 	def get_queryset(self):
# 		return NamesModel.objects.all()

# 	def put(self, request, pk, format=None):
# 		snippet = NamesModel.objects.get(pk=pk)
# 		serializer = NamesSerializer(snippet, data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 		return Response('moma', status=HTTP_200_OK)
		
# 	def delete(self, request, pk, format=None):
# 		snippet = NamesModel.objects.get(pk=pk)
# 		snippet.delete()
# 		return Response('moma', status=HTTP_200_OK)





class GetclientdataView( generics.ListAPIView):
	queryset = ClientsModels.objects.all()
	serializer_class=ClientsSerializer
	permission_classes = [AllowAny]
	
	def get_queryset(self):
		username=self.kwargs['username']
		snippets = ClientsModels.objects.filter(username=username)
		return snippets

class searchedView( generics.ListAPIView):
	# queryset = Job_Posts.objects.all()
	serializer_class=Job_PostsSerializer
	permission_classes = [AllowAny]
	
	def get_queryset(self):
		keyword=self.kwargs['keyword']
		mkoa=self.kwargs['mkoa']
		if mkoa=='all':
			snippets = Job_Posts.objects.filter(title__icontains=keyword)
			return snippets
		else:
			snippets = Job_Posts.objects.filter(title__icontains=keyword, location__icontains=mkoa)
			return snippets
    		


class ChangePasswordView(generics.UpdateAPIView):
        """
        An endpoint for changing password.
        """
        serializer_class = ChangePasswordSerializer
        model = User
        permission_classes = [IsAuthenticated,]

        def get_object(self, queryset=None):
            obj = self.request.user
            return obj

        def update(self, request, *args, **kwargs):
            self.object = self.get_object()
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                # Check old password
                if not self.object.check_password(serializer.data.get("old_password")):
                    return Response({"old_password": ["Wrong password."]}, status=HTTP_400_BAD_REQUEST)
                # set_password also hashes the password that the user will get
                self.object.set_password(serializer.data.get("new_password"))
                self.object.save()
                response = {
                    'status': 'success',
                    'code': HTTP_200_OK,
                    'message': 'Password updated successfully',
                    'data': []
                }

                return Response(response)

            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
class EmployeeViewSet(generics.ListAPIView):
		serializer_class = UserSerializerRetrieve
		
		def get_queryset(self):
			goal=self.kwargs['goal']
			status=self.kwargs['status']

			if status=='username':
    			 return User.objects.filter(username=goal)
			if status=='email':
				 return User.objects.filter(email=goal)



class CategoryFilterView(generics.ListAPIView):
    	# lookup_field="pk"
		serializer_class=Job_PostsSerializer
		permission_classes = [AllowAny]
		filterset_class=CategoryFilter
		filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

		search_fields=['category']
		queryset = categories.objects.all()
