"""Fingerprint URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

# from rest_framework_jwt.views import obtain_jwt_token
from .views import  *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'Clients'


urlpatterns = [
    url('toke_pro/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
    # url(r'^$', numberGetview.as_view(), name='numberCreate'),
    url(r'^UserCreate/$', CreateUserView.as_view(), name='nubergen'),
    url(r'^getalljobs/$', getalljobsView.as_view(), name='nubergen'),
    url(r'^filterwork/$', CategoryFilterView.as_view(), name='filterwork'),
    url(r'^customer/$', TokenValidatorAPIView.as_view(), name='token'),
    url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
    url(r'^postClient/(?P<username>.+)/$', Job_requestsView.as_view(), name='data'),
    url(r'^checktoken/$', TokenValidatorAPIView.as_view(), name='hgv'),
    url(r'^allusers/(?P<goal>.+)/(?P<status>.+)/$', EmployeeViewSet.as_view(), name='hgv'),
    url(r'^jobpost/(?P<company>.+)/$', Job_PostsView.as_view(), name='data'),
    url(r'^companybio/(?P<username>.+)/$', CompanybioView.as_view(), name='data'),
    url(r'^clientcreate/$', ClientView.as_view(), name='data'),
    url(r'^clientcreate1/$', ClientView1.as_view(), name='data'),
    url(r'^Viewnormaluser/$', ClientViewnormaluser.as_view(), name='data'),
    url(r'^clientsdata/(?P<username>.+)/$', GetclientdataView.as_view(), name='data'),
    url(r'^qualifaication/(?P<username>.+)/$', qualifaicationView.as_view(), name='data'),
    url(r'^skills/(?P<username>.+)/$', SkillsView.as_view(), name='data'),
    url(r'^Experience/(?P<username>.+)/$', ExperienceView.as_view(), name='data'),
    url(r'^Sendfile/(?P<username>.+)/$', CVView.as_view(), name='data'),
    url(r'^cvpull/(?P<username>.+)/$', CVView.as_view(), name='data'),
    url(r'^package/(?P<username>.+)/$', packageview.as_view(), name='data'),
    url(r'^jobposthome/(?P<username>.+)/$', jobposthomeView.as_view(), name='data'),
    url(r'^searchjobs/(?P<category>.+)/(?P<momo>.+)/$', searchjobsView.as_view(), name='data'),
    url(r'^search/(?P<username>.+)/(?P<values>.+)/$', SearchJobview.as_view(), name='data'),
    url(r'^postapply/(?P<username>.+)/(?P<pk>.+)/$', ApplyJobview.as_view(), name='data'),
    url(r'^postapplied/(?P<company>.+)/$', AppliedJobview.as_view(), name='data'),
    url(r'^categories/(?P<username>.+)/$', CategoryView.as_view(), name='categories'),
    url(r'^Emails/$', EmailsView.as_view(), name='categories'),
    url(r'^postalert/(?P<username>.+)/$', Job_Posts1View.as_view(), name='data'),
    url(r'^uploadprofile/(?P<username>.+)/$', ClientProfileView.as_view(), name='profile'),
    url(r'^empdata/(?P<username>.+)/$', GetclientdataView.as_view(), name='data'),
    url(r'^searched/(?P<keyword>.+)/(?P<mkoa>.+)/$', searchedView.as_view(), name='data'),
    url(r'^state/(?P<username>.+)/(?P<pk>.+)/$', UpdatestatusView.as_view(), name='data'),
    url(r'^deleteapplied/(?P<action>.+)/(?P<pk>.+)/$', Deleteview.as_view(), name='data'),
    url(r'^updatuser/(?P<username>.+)/$', Upadateview.as_view(), name='data'),
    url(r'^jobdetails/(?P<pk>.+)/$', JobDetailsview.as_view(), name='data'),
    url(r'^changepassword/$', ChangePasswordView.as_view(), name='WorkersTransactions'),
    url(r'^jobapplicationdetails/(?P<pk>.+)/$', jobapplictionsView.as_view(), name='data'),
  


]