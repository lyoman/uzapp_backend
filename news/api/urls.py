from django.conf.urls import url
from django.contrib import admin

from .views import (
    NewCreateAPIView,
    NewListAPIView,
    NewDetailAPIView,
    NewUpdateAPIView,
    NewDeleteAPIView,
    ReaderDetailAPIView,
    ReaderListAPIView,
	)

urlpatterns = [
    url(r'^$', NewListAPIView.as_view(), name='news'),
    url(r'^readers/$', ReaderListAPIView.as_view(), name='news1'),
    url(r'^reader/(?P<pk>[\d]+)/$', ReaderDetailAPIView.as_view(), name='detail1'),
    url(r'^(?P<pk>[\d]+)/$', NewDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>[\d]+)/delete/$', NewDeleteAPIView.as_view(), name="delete"),
    url(r'^(?P<pk>[\d]+)/edit/$', NewUpdateAPIView.as_view(), name='update'),
    url(r'^create/$', NewCreateAPIView.as_view(), name="addnews"),
]