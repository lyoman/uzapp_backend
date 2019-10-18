from rest_framework.serializers import (
        HyperlinkedIdentityField,
        ModelSerializer,
        SerializerMethodField,
        )

from django.contrib.auth.models import User
from django.db import models
from restaurants.models import Restaurant, Meal
from users.api.serializers import UserDetailSerializer






#Creating an new
class RestaurantCreateUpdateSerializer(ModelSerializer):
    user   = models.ForeignKey(User, default=1, on_delete = models.CASCADE)
    class Meta:
        model = Restaurant
        fields = [
            'user',
            'name',
            'location',
            'lat',
            'lng',
        ]


new_detail_url = HyperlinkedIdentityField(
        view_name='restaurants-api:detail',
        lookup_field='pk'#or primary key <pk>
    )

# Restaurant Details
class RestaurantDetailSerializer(ModelSerializer):
    url    = new_detail_url
    user   = UserDetailSerializer(read_only=True)
    class Meta:
        model = Restaurant
        fields = [
            'url',
            'id',
            'user',
            'name',
            'location',
            'lat',
            'lng',
            'updated',
            'timestamp',
        ]

# All Restaurant List
class RestaurantListSerializer(ModelSerializer):
    url = new_detail_url
    UserDetailSerializer(read_only=True)
    delete_url = HyperlinkedIdentityField(
        view_name='restaurants-api:delete',
        lookup_field='pk'#or primary key <pk>
    )
    class Meta:
        model = Restaurant
        fields = [
            'url',
            'id',
            'user',
            'name',
            'location',
            'lat',
            'lng',
            'updated',
            'timestamp',
            'delete_url', 
        ]

    

#Creating a Meal
class MealCreateUpdateSerializer(ModelSerializer):
    restaurant   = models.ForeignKey(Restaurant, default=1, on_delete = models.CASCADE)
    class Meta:
        model = Meal
        fields = [
            'restaurant',
            'name',
            'price',
        ]


new_detail_url = HyperlinkedIdentityField(
        view_name='restaurants-api:detail1',
        lookup_field='pk'#or primary key <pk>
    )

# Meal Details
class MealDetailSerializer(ModelSerializer):
    url          = new_detail_url
    restaurant   = RestaurantDetailSerializer(read_only=True)
    class Meta:
        model = Meal
        fields = [
            'url',
            'id',
            'name',
            'price',
            'updated',
            'timestamp',
            'restaurant',
        ]

# All Meal List
class MealListSerializer(ModelSerializer):
    url        = new_detail_url
    restaurant = RestaurantDetailSerializer(read_only=True)
    delete_url = HyperlinkedIdentityField(
        view_name='restaurants-api:delete1',
        lookup_field='pk'#or primary key <pk>
    )
    class Meta:
        model = Meal
        fields = [
            'url',
            'id',
            'name',
            'price',
            'updated',
            'timestamp',
            'delete_url', 
            'restaurant',
        ]
