from django.conf.urls import url
from django.contrib import admin

from .views import (
    GuestCreateAPIView,
    GuestListAPIView,
    GuestDetailAPIView,
    GuestUpdateAPIView,
    GuestDeleteAPIView,
	)

urlpatterns = [
    url(r'^$', GuestListAPIView.as_view(), name='guests'),
    url(r'^(?P<pk>[\d]+)/$', GuestDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>[\d]+)/delete/$', GuestDeleteAPIView.as_view(), name="delete"),
    url(r'^(?P<pk>[\d]+)/edit/$', GuestUpdateAPIView.as_view(), name='update'),
    url(r'^register/$', GuestCreateAPIView.as_view(), name="create"),
]