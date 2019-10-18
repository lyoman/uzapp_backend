from django.conf.urls import url
# from django.urls import path
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token# , CustomAuthToken
from django.urls import path
# from rest_framework_simplejwt import views as jwt_views

from .views import (
    StudentLoginAPIView,
    StudentCreateAPIView,
    StudentListAPIView
    )


urlpatterns = [
    url(r'^api/auth/token/', obtain_jwt_token),
    url(r'^login/$', StudentLoginAPIView.as_view(), name='login1'),
    url(r'^register/$', StudentCreateAPIView.as_view(), name='register1'),
    url(r'^$', StudentListAPIView.as_view(), name='student'),
] 