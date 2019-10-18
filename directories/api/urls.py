from django.conf.urls import url
from django.contrib import admin

from .views import (
    PhoneNumberCreateAPIView,
    PhoneNumberDetailAPIView,
    PhoneNumberUpdateAPIView,
    PhoneNumberDeleteAPIView,
    PhoneNumberListAPIView,
    DepartmentDetailAPIView,
    FacultyDetailAPIView,
	)

urlpatterns = [
    url(r'^$', PhoneNumberListAPIView.as_view(), name='phones'),
    url(r'^(?P<pk>[\d]+)/$', PhoneNumberDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>[\d]+)/delete/$', PhoneNumberDeleteAPIView.as_view(), name="delete"),
    url(r'^(?P<pk>[\d]+)/edit/$', PhoneNumberUpdateAPIView.as_view(), name='update'),
    url(r'^create/$', PhoneNumberCreateAPIView.as_view(), name="create"),
    url(r'^departments/$', DepartmentDetailAPIView.as_view(), name='department'),
    url(r'^faculties/$', FacultyDetailAPIView.as_view(), name='faculty'),
]