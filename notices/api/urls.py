from django.conf.urls import url
from django.contrib import admin

from .views import (
    NoticeCreateAPIView,
    NoticeListAPIView,
    NoticeDetailAPIView,
    NoticeUpdateAPIView,
    NoticeDeleteAPIView,
	)

urlpatterns = [
    url(r'^$', NoticeListAPIView.as_view(), name='notices'),
    url(r'^(?P<pk>[\d]+)/$', NoticeDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>[\d]+)/delete/$', NoticeDeleteAPIView.as_view(), name="delete"),
    url(r'^(?P<pk>[\d]+)/edit/$', NoticeUpdateAPIView.as_view(), name='update'),
    url(r'^create/$', NoticeCreateAPIView.as_view(), name="addnotice"),
]