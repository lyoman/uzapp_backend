from rest_framework.serializers import (
        HyperlinkedIdentityField,
        ModelSerializer,
        SerializerMethodField,
        )

from django.contrib.auth.models import User
from django.db import models
from ambulance.models import AmbulanceRequests
from users.api.serializers import UserDetailSerializer
    

#Creating an new
class AmbulanceCreateUpdateSerializer(ModelSerializer):
    user   = models.ForeignKey(User, default=1, on_delete = models.CASCADE)
    lat    = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    lng    = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    class Meta:
        model = AmbulanceRequests
        fields = [
            'user',
            'location',
            'problem',
            'status',
            'lat',
            'lng',
        ]


new_detail_url = HyperlinkedIdentityField(
        view_name='ambulance-api:detail',
        lookup_field='pk'#or primary key <pk>
    )

# Ambulance Details
class AmbulanceDetailSerializer(ModelSerializer):
    url    = new_detail_url
    user   = UserDetailSerializer(read_only=True)
    class Meta:
        model = AmbulanceRequests
        fields = [
            'url',
            'id',
            'user',
            'status',
            'location',
            'problem',
            'lat',
            'lng',
            'timestamp',
        ]

# All Ambulance List
class AmbulanceListSerializer(ModelSerializer):
    url  = new_detail_url
    user = UserDetailSerializer(read_only=True)
    delete_url = HyperlinkedIdentityField(
        view_name='ambulance-api:delete',
        lookup_field='pk'#or primary key <pk>
    )
    class Meta:
        model = AmbulanceRequests
        fields = [
            'url',
            'id',
            'user',
            'status',
            'location',
            'problem',
            'lat',
            'lng',
            'timestamp',
            'delete_url', 
        ]
