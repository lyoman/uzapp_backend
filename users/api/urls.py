from django.conf.urls import url
# from django.urls import path
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token# , CustomAuthToken
from django.urls import path
# from rest_framework_simplejwt import views as jwt_views

from .views import (
    UserLoginAPIView,
    UserCreateAPIView,
    UserListAPIView
    )


urlpatterns = [
    url(r'^api/auth/token/', obtain_jwt_token),
    url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
    url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
    url(r'^users/$', UserListAPIView.as_view(), name='user'),
] 