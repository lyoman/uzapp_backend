from django.conf.urls import url
from django.contrib import admin

from .views import (
    FoodOrderCreateAPIView,
    FoodOrderListAPIView,
    FoodOrderDetailAPIView,
    FoodOrderUpdateAPIView,
    FoodOrderDeleteAPIView,
	)

urlpatterns = [
    url(r'^$', FoodOrderListAPIView.as_view(), name='list'),
    url(r'^(?P<pk>[\d]+)/$', FoodOrderDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>[\d]+)/delete/$', FoodOrderDeleteAPIView.as_view(), name="delete"),
    url(r'^(?P<pk>[\d]+)/edit/$', FoodOrderUpdateAPIView.as_view(), name='update'),
    url(r'^create/$', FoodOrderCreateAPIView.as_view(), name="add"),
]