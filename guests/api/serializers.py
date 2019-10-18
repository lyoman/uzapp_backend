from rest_framework.serializers import (
        HyperlinkedIdentityField,
        ModelSerializer,
        SerializerMethodField,
        )

from django.db import models
from guests.models import Guest
    

#Creating an new
class GuestCreateUpdateSerializer(ModelSerializer):
    lat         = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    lng         = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    class Meta:
        model = Guest
        fields = [
            'name',
            'phone',
            'lat',
            'lng',
        ]


new_detail_url = HyperlinkedIdentityField(
        view_name='guests-api:detail',
        lookup_field='pk'#or primary key <pk>
    )

# Guest Details
class GuestDetailSerializer(ModelSerializer):
    url    = new_detail_url
    class Meta:
        model = Guest
        fields = [
            'url',
            'id',
            'name',
            'phone',
            'lat',
            'lng',
            'updated',
            'timestamp',
        ]

# All Guest List
class GuestListSerializer(ModelSerializer):
    url = new_detail_url
    delete_url = HyperlinkedIdentityField(
        view_name='guests-api:delete',
        lookup_field='pk'#or primary key <pk>
    )
    class Meta:
        model = Guest
        fields = [
            'url',
            'id',
            'name',
            'phone',
            'lat',
            'lng',
            'updated',
            'timestamp',
            'delete_url', 
        ]
