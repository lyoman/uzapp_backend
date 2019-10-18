from rest_framework.serializers import (
        HyperlinkedIdentityField,
        ModelSerializer,
        SerializerMethodField,
        )

from django.contrib.auth.models import User
from django.db import models
from healthtips.models import Healthtip
from users.api.serializers import UserDetailSerializer
  
#Creating an new
class HealthtipsCreateUpdateSerializer(ModelSerializer):
    user   = models.ForeignKey(User, default=1, on_delete = models.CASCADE)
    class Meta:
        model = Healthtip
        fields = [
            'user',
            'name',
            'details',
            'category',
        ]


new_detail_url = HyperlinkedIdentityField(
        view_name='healthtips-api:detail',
        lookup_field='pk'#or primary key <pk>
    )

# Healthtip Details
class HealthtipsDetailSerializer(ModelSerializer):
    url    = new_detail_url
    user   = UserDetailSerializer(read_only=True)
    class Meta:
        model = Healthtip
        fields = [
            'url',
            'id',
            'user',
            'name',
            'category',
            'details',
            'timestamp',
        ]

# All Healthtips List
class HealthtipsListSerializer(ModelSerializer):
    url = new_detail_url
    user = UserDetailSerializer(read_only=True)
    delete_url = HyperlinkedIdentityField(
        view_name='healthtips-api:delete',
        lookup_field='pk'#or primary key <pk>
    )
    class Meta:
        model = Healthtip
        fields = [
            'url',
            'id',
            'user',
            'name',
            'category',
            'details',
            'timestamp',
            'delete_url', 
        ]