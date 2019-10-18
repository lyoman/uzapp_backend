from rest_framework.serializers import (
        HyperlinkedIdentityField,
        ModelSerializer,
        SerializerMethodField,
        )

from django.contrib.auth.models import User
from django.db import models
from foodordering.models import FoodOrder
from restaurants.models import Meal
from users.api.serializers import UserDetailSerializer
from restaurants.api.serializers import MealDetailSerializer
    

#Creating an new
class FoodOrderCreateUpdateSerializer(ModelSerializer):
    user   = models.ForeignKey(User, default=1, on_delete = models.CASCADE)
    meal   = models.ForeignKey(Meal, default=1, on_delete = models.CASCADE)
    class Meta:
        model = FoodOrder
        fields = [
            'user',
            'meal',
            'amount',
            'status',
            'location',
            'lat',
            'lng',
            'refrence',
        ]


new_detail_url = HyperlinkedIdentityField(
        view_name='foodordering-api:detail',
        lookup_field='pk'#or primary key <pk>
    )

# FoodOrder Details
class FoodOrderDetailSerializer(ModelSerializer):
    url    = new_detail_url
    user   = UserDetailSerializer(read_only=True)
    meal   = MealDetailSerializer(read_only=True)
    class Meta:
        model = FoodOrder
        fields = [
            'url',
            'id',
            'user',
            'meal',
            'amount',
            'status',
            'location',
            'lat',
            'lng',
            'refrence',
            'timestamp',
        ]

# All FoodOrder List
class FoodOrderListSerializer(ModelSerializer):
    url = new_detail_url
    user = UserDetailSerializer(read_only=True)
    meal = MealDetailSerializer(read_only=True)
    delete_url = HyperlinkedIdentityField(
        view_name='foodordering-api:delete',
        lookup_field='pk'#or primary key <pk>
    )
    class Meta:
        model = FoodOrder
        fields = [
            'url',
            'id',
            'user',
            'meal',
            'amount',
            'status',
            'location',
            'lat',
            'lng',
            'refrence',
            'timestamp',
            'delete_url', 
        ]
