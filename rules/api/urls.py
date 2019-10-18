from django.conf.urls import url
from django.contrib import admin

from .views import (
    RuleCreateAPIView,
    RuleListAPIView,
    RuleDetailAPIView,
    RuleUpdateAPIView,
    RuleDeleteAPIView,
	)

urlpatterns = [
    url(r'^$', RuleListAPIView.as_view(), name='rules'),
    url(r'^(?P<pk>[\d]+)/$', RuleDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>[\d]+)/delete/$', RuleDeleteAPIView.as_view(), name="delete"),
    url(r'^(?P<pk>[\d]+)/edit/$', RuleUpdateAPIView.as_view(), name='update'),
    url(r'^create/$', RuleCreateAPIView.as_view(), name="addrules"),
]