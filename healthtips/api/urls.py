from django.conf.urls import url
from django.contrib import admin

from .views import (
    HealthtipCreateAPIView,
    HealthtipListAPIView,
    HealthtipDetailAPIView,
    HealthtipUpdateAPIView,
    HealthtipDeleteAPIView,
	)

urlpatterns = [
    url(r'^$', HealthtipListAPIView.as_view(), name='healthtips'),
    url(r'^(?P<pk>[\d]+)/$', HealthtipDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>[\d]+)/delete/$', HealthtipDeleteAPIView.as_view(), name="delete"),
    url(r'^(?P<pk>[\d]+)/edit/$', HealthtipUpdateAPIView.as_view(), name='update'),
    url(r'^create/$', HealthtipCreateAPIView.as_view(), name="addhealthtips"),
]