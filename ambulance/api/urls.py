from django.conf.urls import url
from django.contrib import admin

from .views import (
    AmbulanceCreateAPIView,
    AmbulanceListAPIView,
    AmbulanceDetailAPIView,
    AmbulanceUpdateAPIView,
    AmbulanceDeleteAPIView,
	)

urlpatterns = [
    url(r'^$', AmbulanceListAPIView.as_view(), name='ambulances'),
    url(r'^(?P<pk>[\d]+)/$', AmbulanceDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>[\d]+)/delete/$', AmbulanceDeleteAPIView.as_view(), name="delete"),
    url(r'^(?P<pk>[\d]+)/edit/$', AmbulanceUpdateAPIView.as_view(), name='update'),
    url(r'^create/$', AmbulanceCreateAPIView.as_view(), name="addambulance"),
]