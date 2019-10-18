from django.conf.urls import url
from django.contrib import admin

from .views import (
    RestaurantCreateAPIView,
    RestaurantListAPIView,
    RestaurantDetailAPIView,
    RestaurantUpdateAPIView,
    RestaurantDeleteAPIView,

    # Meals
    MealCreateAPIView,
    MealListAPIView,
    MealDetailAPIView,
    MealUpdateAPIView,
    MealDeleteAPIView,
	)

urlpatterns = [
    url(r'^$', RestaurantListAPIView.as_view(), name='restaurants'),
    url(r'^(?P<pk>[\d]+)/$', RestaurantDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>[\d]+)/delete/$', RestaurantDeleteAPIView.as_view(), name="delete"),
    url(r'^(?P<pk>[\d]+)/edit/$', RestaurantUpdateAPIView.as_view(), name='update'),
    url(r'^create/$', RestaurantCreateAPIView.as_view(), name="addrestaurant"),

    # Meals
    url(r'^meals/$', MealListAPIView.as_view(), name='meals'),
    url(r'^meals/(?P<pk>[\d]+)/$', MealDetailAPIView.as_view(), name='detail1'),
    url(r'^meals/(?P<pk>[\d]+)/delete/$', MealDeleteAPIView.as_view(), name="delete1"),
    url(r'^meals/(?P<pk>[\d]+)/edit/$', MealUpdateAPIView.as_view(), name='update1'),
    url(r'^meals/create/$', MealCreateAPIView.as_view(), name="addmeal"),
]