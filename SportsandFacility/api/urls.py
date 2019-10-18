from django.conf.urls import url
from django.contrib import admin

from .views import (
    EventCreateAPIView,
    EventDetailAPIView,
    EventUpdateAPIView,
    EventDeleteAPIView,
    EventListAPIView,
    FacilityDetailAPIView,
    SportsandClubDetailAPIView,
    CategoryDetailAPIView,
	)

urlpatterns = [
    url(r'^$', EventListAPIView.as_view(), name='events'),
    url(r'^(?P<pk>[\d]+)/$', EventDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>[\d]+)/delete/$', EventDeleteAPIView.as_view(), name="delete"),
    url(r'^(?P<pk>[\d]+)/edit/$', EventUpdateAPIView.as_view(), name='update'),
    url(r'^create/$', EventCreateAPIView.as_view(), name="create"),
    url(r'^facilities/$', FacilityDetailAPIView.as_view(), name='facility'),
    url(r'^sports/$', SportsandClubDetailAPIView.as_view(), name='sports'),
    url(r'^sportcategory/$', CategoryDetailAPIView.as_view(), name='category'),
]