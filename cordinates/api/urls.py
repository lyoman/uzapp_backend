from django.conf.urls import url
from django.contrib import admin

from .views import (
    CordinateCreateAPIView,
    CordinateListAPIView,
    CordinateDetailAPIView,
    CordinateUpdateAPIView,
    CordinateDeleteAPIView,
	)

urlpatterns = [
    url(r'^$', CordinateListAPIView.as_view(), name='cordinates'),
    url(r'^(?P<pk>[\d]+)/$', CordinateDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>[\d]+)/delete/$', CordinateDeleteAPIView.as_view(), name="delete"),
    url(r'^(?P<pk>[\d]+)/edit/$', CordinateUpdateAPIView.as_view(), name='update'),
    url(r'^create/$', CordinateCreateAPIView.as_view(), name="create"),
]