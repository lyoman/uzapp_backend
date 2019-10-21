from django.conf.urls import url
from django.contrib import admin

from .views import (
    LostCreateAPIView,
    LostListAPIView,
    LostDetailAPIView,
    LostUpdateAPIView,
    LostDeleteAPIView,
	)

urlpatterns = [
    url(r'^$', LostListAPIView.as_view(), name='lost'),
    url(r'^(?P<pk>[\d]+)/$', LostDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>[\d]+)/delete/$', LostDeleteAPIView.as_view(), name="delete"),
    url(r'^(?P<pk>[\d]+)/edit/$', LostUpdateAPIView.as_view(), name='update'),
    url(r'^create/$', LostCreateAPIView.as_view(), name="addlost"),
]