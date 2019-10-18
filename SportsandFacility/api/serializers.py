from django.contrib.auth.models import User
from django.db import models

from rest_framework.serializers import (
        HyperlinkedIdentityField,
        ModelSerializer,
        SerializerMethodField,
        )

from SportsandFacility.models import  Facility, SportsandClub, Event, Category
from users.api.serializers import UserDetailSerializer



class FacilityDetailSerializer(ModelSerializer):
    class Meta:
        model = Facility
        fields = [
         
            'id',
            'name',
            'capacity',
            'specification',
            'location',
            'lat',
            'lng',
            'timestamp',
            'updated',
            ]


#Creating an ApplyMedical
class EventCreateUpdateSerializer(ModelSerializer):
    venue       = models.ForeignKey(Facility, default=1, on_delete = models.CASCADE)
    event_date  = models.DateField(auto_now=False, auto_now_add=True)
    event_time  = models.TimeField(auto_now=False, auto_now_add=True)
    class Meta:
        model = Event
        fields = [
            'title',
            'venue',
            'custom_venue',
            'description',
            'link_url',
            'event_date',
            'event_time',
        ]


apply_detail_url = HyperlinkedIdentityField(
        view_name='SportsandFacility-api:detail',
        lookup_field='pk'#or primary key <pk>
    )

class CategoryDetailSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = [
         
            'id',
            'name',
            'timestamp',
            'updated',
            ]


class SportsandClubDetailSerializer(ModelSerializer):
    category = CategoryDetailSerializer(read_only=True)
    facility = FacilityDetailSerializer(read_only=True)
    coach    = UserDetailSerializer(read_only=True)
    # captain  = UserDetailSerializer(read_only=True)
    class Meta:
        model = SportsandClub
        fields = [
            'id',
            'category',
            'facility',
            'coach',
            'captain',
            'name',
            'timestamp',
            'updated',
            ]


class EventDetailSerializer(ModelSerializer):
    url       = apply_detail_url
    venue     = FacilityDetailSerializer(read_only=True)

    class Meta:
        model = Event
        fields = [
            'url',
            'id',
            'title',
            'venue',
            'description',
            'custom_venue',
            'timestamp',
            'updated',
            'event_date',
            'event_time',
            'link_url',
        ]
    

class EventListSerializer(ModelSerializer):
    url      = apply_detail_url
    venue    = FacilityDetailSerializer(read_only=True)
    delete_url = HyperlinkedIdentityField(
        view_name='SportsandFacility-api:delete',
        lookup_field='pk'#or primary key <pk>
    )
    class Meta:
        model  = Event
        fields = [
            'url',
            'id',
            'title',
            'venue',
            'description',
            'custom_venue',
            'event_date',
            'event_time',
            'link_url',
            'timestamp',
            'updated',
            'delete_url', 
        ]