from django.conf.urls import url
from django.contrib import admin

from .views import (
    HomeCreateAPIView,
    HomeListAPIView,
    HomeDetailAPIView,
    HomeUpdateAPIView,
    HomeDeleteAPIView,
	)

urlpatterns = [
    url(r'^$', HomeListAPIView.as_view(), name='home'),
    url(r'^(?P<pk>[\d]+)/$', HomeDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>[\d]+)/delete/$', HomeDeleteAPIView.as_view(), name="delete"),
    url(r'^(?P<pk>[\d]+)/edit/$', HomeUpdateAPIView.as_view(), name='update'),
    url(r'^create/$', HomeCreateAPIView.as_view(), name="addhome"),
]