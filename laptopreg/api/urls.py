from django.conf.urls import url
from django.contrib import admin

from .views import (
    LaptopsRegisterCreateAPIView,
    LaptopsRegisterListAPIView,
    LaptopsRegisterDetailAPIView,
    LaptopsRegisterUpdateAPIView,
    LaptopsRegisterDeleteAPIView,
	)

urlpatterns = [
    url(r'^$', LaptopsRegisterListAPIView.as_view(), name='list'),
    url(r'^(?P<pk>[\d]+)/$', LaptopsRegisterDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>[\d]+)/delete/$', LaptopsRegisterDeleteAPIView.as_view(), name="delete"),
    url(r'^(?P<pk>[\d]+)/edit/$', LaptopsRegisterUpdateAPIView.as_view(), name='update'),
    url(r'^create/$', LaptopsRegisterCreateAPIView.as_view(), name="add"),
]