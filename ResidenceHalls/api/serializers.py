from django.contrib.auth.models import User
from django.db import models

from rest_framework.serializers import (
        HyperlinkedIdentityField,
        ModelSerializer,
        SerializerMethodField,
        )

from ResidenceHalls.models import  RezHall, Commitie, Janitor, Warden
from users.api.serializers import UserDetailSerializer


#Creating an ApplyMedical
class RezHallCreateUpdateSerializer(ModelSerializer):
    janitor   = models.ForeignKey(Janitor, default=1, on_delete = models.CASCADE)
    warden    = models.ForeignKey(Warden, default=1, on_delete = models.CASCADE)
    commitie  = models.ForeignKey(Commitie, default=1, on_delete = models.CASCADE)
    lat       = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    lng       = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    class Meta:
        model = RezHall
        fields = [
            'name',
            'capacity',
            'location',
            'lat',
            'lng',
            'janitor',
            'warden',
            'commitie',
        ]


apply_detail_url = HyperlinkedIdentityField(
        view_name='ResidenceHalls-api:detail',
        lookup_field='pk'#or primary key <pk>
    )

class WardenDetailSerializer(ModelSerializer):
    user = UserDetailSerializer(read_only=True)
    class Meta:
        model = Warden
        fields = [
         
            'id',
            'user',
            # 'name',
            'timestamp',
            'updated',
            ]


class CommitieDetailSerializer(ModelSerializer):
    user = UserDetailSerializer(read_only=True)
    class Meta:
        model = Commitie
        fields = [
            'id',
            'user',
            'name',
            'role',
            'timestamp',
            'updated',
            ]


class JanitorDetailSerializer(ModelSerializer):
    user = UserDetailSerializer(read_only=True)
    class Meta:
        model = Janitor
        fields = [
         
            'id',
            'user',
            'name',
            'timestamp',
            'updated',
            ]


class RezHallDetailSerializer(ModelSerializer):
    url        = apply_detail_url
    janitor    = JanitorDetailSerializer(read_only=True)
    warden     = WardenDetailSerializer(read_only=True)
    commitie   = CommitieDetailSerializer(read_only=True)

    class Meta:
        model = RezHall
        fields = [
            'url',
            'id',
            'name',
            'capacity',
            'location',
            'lat',
            'lng',
            'timestamp',
            'updated',
            'janitor',
            'warden',
            'commitie',
        ]
    

class RezHallListSerializer(ModelSerializer):
    url        = apply_detail_url
    janitor    = JanitorDetailSerializer(read_only=True)
    warden     = WardenDetailSerializer(read_only=True)
    commitie   = CommitieDetailSerializer(read_only=True)
    delete_url = HyperlinkedIdentityField(
        view_name='ResidenceHalls-api:delete',
        lookup_field='pk'#or primary key <pk>
    )
    class Meta:
        model  = RezHall
        fields = [
            'url',
            'id',
            'name',
            'capacity',
            'location',
            'lat',
            'lng',
            'warden',
            'janitor',
            'commitie',
            'janitor',
            'timestamp',
            'updated',
            'delete_url', 
        ]