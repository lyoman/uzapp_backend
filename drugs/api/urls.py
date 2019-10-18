from django.conf.urls import url
from django.contrib import admin

from .views import (
    DrugCreateAPIView,
    DrugListAPIView,
    DrugDetailAPIView,
    DrugUpdateAPIView,
    DrugDeleteAPIView,
	)

urlpatterns = [
    url(r'^$', DrugListAPIView.as_view(), name='drugs'),
    url(r'^(?P<pk>[\d]+)/$', DrugDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>[\d]+)/delete/$', DrugDeleteAPIView.as_view(), name="delete"),
    url(r'^(?P<pk>[\d]+)/edit/$', DrugUpdateAPIView.as_view(), name='update'),
    url(r'^create/$', DrugCreateAPIView.as_view(), name="addfaqs"),
]