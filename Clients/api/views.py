from ..models import *
from .serializers import *
from django.contrib.auth import get_user_model

from datetime import datetime, timedelta
from django.utils import timezone
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated

import os
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
import json


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


class ClientView(generics.CreateAPIView, generics.ListAPIView):
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
	serializer_class = Job_requestsSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		user=self.kwargs['pk']
		return Job_requests.objects.filter(user=user)

	def post(self, request, *args, **kwargs):
		data = request.data
		serializer = Job_requestsSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			mon = serializer.save()

			
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
			# position = serializer.validated_data['position']
			City = serializer.validated_data['City']
			instagram_url = serializer.validated_data['instagram_url']
			spark_url = serializer.validated_data['spark_url']
			Linkedin = serializer.validated_data['Linkedin']
			Country_code = serializer.validated_data['Country_code']
			twitter_url = serializer.validated_data['twitter_url']
			pinterest_url = serializer.validated_data['pinterest_url']
			faceboo_url = serializer.validated_data['faceboo_url']

			moxt=ClientsModels.objects.filter(username=username).update(Linkedin=Linkedin, Country=Country, client_first_name=client_first_name, client_second_name='client_second_name', client_third_name='client_third_name', Country_code='Country_code', Birthdate='Birthdate', Complete_address='Complete_address', Nationality='Nationality', City='City', faceboo_url='faceboo_url', instagram_url='instagram_url', spark_url='spark_url', twitter_url='twitter_url', pinterest_url='pinterest_url', Mobile_number='Mobile_number')
			# mon = serializer.save()

			return Response(serializer.validated_data)
	


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
		return CV.objects.all()

class Job_PostsView(generics.CreateAPIView, generics.ListAPIView):
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