from django.conf.urls import url
from django.contrib import admin

from .views import (
    RezHallCreateAPIView,
    RezHallDetailAPIView,
    RezHallUpdateAPIView,
    RezHallDeleteAPIView,
    RezHallListAPIView,
    JanitorDetailAPIView,
    WardenDetailAPIView,
    CommitieDetailAPIView,
	)

urlpatterns = [
    url(r'^$', RezHallListAPIView.as_view(), name='halls'),
    url(r'^(?P<pk>[\d]+)/$', RezHallDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>[\d]+)/delete/$', RezHallDeleteAPIView.as_view(), name="delete"),
    url(r'^(?P<pk>[\d]+)/edit/$', RezHallUpdateAPIView.as_view(), name='update'),
    url(r'^create/$', RezHallCreateAPIView.as_view(), name="create"),
    url(r'^janitors/$', JanitorDetailAPIView.as_view(), name='janitor'),
    url(r'^wardens/$', WardenDetailAPIView.as_view(), name='warden'),
    url(r'^commities/$', CommitieDetailAPIView.as_view(), name='commitie'),
]