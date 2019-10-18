from django.conf.urls import url
from django.contrib import admin

from .views import (
    FaqCreateAPIView,
    FaqListAPIView,
    FaqDetailAPIView,
    FaqUpdateAPIView,
    FaqDeleteAPIView,
	)

urlpatterns = [
    url(r'^$', FaqListAPIView.as_view(), name='faqs'),
    url(r'^(?P<pk>[\d]+)/$', FaqDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>[\d]+)/delete/$', FaqDeleteAPIView.as_view(), name="delete"),
    url(r'^(?P<pk>[\d]+)/edit/$', FaqUpdateAPIView.as_view(), name='update'),
    url(r'^create/$', FaqCreateAPIView.as_view(), name="addfaqs"),
]