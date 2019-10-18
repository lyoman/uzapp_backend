from rest_framework.serializers import (
        HyperlinkedIdentityField,
        ModelSerializer,
        SerializerMethodField,
        )

from django.db import models
from cordinates.models import Cordinate
    

#Creating an new
class CordinateCreateUpdateSerializer(ModelSerializer):
    lat         = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    lng         = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    class Meta:
        model = Cordinate
        fields = [
            'name',
            'icon',
            'location',
            'lat',
            'lng',
        ]


new_detail_url = HyperlinkedIdentityField(
        view_name='cordinates-api:detail',
        lookup_field='pk'#or primary key <pk>
    )

# Cordinate Details
class CordinateDetailSerializer(ModelSerializer):
    url    = new_detail_url
    class Meta:
        model = Cordinate
        fields = [
            'url',
            'id',
            'name',
            'icon',
            'location',
            'lat',
            'lng',
            'updated',
            'timestamp',
        ]

# All Cordinate List
class CordinateListSerializer(ModelSerializer):
    url = new_detail_url
    delete_url = HyperlinkedIdentityField(
        view_name='cordinates-api:delete',
        lookup_field='pk'#or primary key <pk>
    )
    class Meta:
        model = Cordinate
        fields = [
            'url',
            'id',
            'name',
            'icon',
            'location',
            'lat',
            'lng',
            'updated',
            'timestamp',
            'delete_url', 
        ]
