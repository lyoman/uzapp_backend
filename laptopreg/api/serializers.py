from rest_framework.serializers import (
        HyperlinkedIdentityField,
        ModelSerializer,
        SerializerMethodField,
        )

from django.contrib.auth.models import User
from django.db import models
from laptopreg.models import LaptopsRegister
from users.api.serializers import UserDetailSerializer
    

#Creating an new
class LaptopsRegisterCreateUpdateSerializer(ModelSerializer):
    user   = models.ForeignKey(User, default=1, on_delete = models.CASCADE)
    class Meta:
        model = LaptopsRegister
        fields = [
            'user',
            'laptopname',
            'color',
            'serialnumber',
        ]


new_detail_url = HyperlinkedIdentityField(
        view_name='laptopreg-api:detail',
        lookup_field='pk'#or primary key <pk>
    )

# LaptopsRegister Details
class LaptopsRegisterDetailSerializer(ModelSerializer):
    url    = new_detail_url
    user   = UserDetailSerializer(read_only=True)
    class Meta:
        model = LaptopsRegister
        fields = [
            'url',
            'id',
            'user',
            'laptopname',
            'color',
            'serialnumber',
            'updated',
            'timestamp',
        ]

# All LaptopsRegister List
class LaptopsRegisterListSerializer(ModelSerializer):
    url = new_detail_url
    user = UserDetailSerializer(read_only=True)
    delete_url = HyperlinkedIdentityField(
        view_name='laptopreg-api:delete',
        lookup_field='pk'#or primary key <pk>
    )
    class Meta:
        model = LaptopsRegister
        fields = [
            'url',
            'id',
            'user',
            'laptopname',
            'color',
            'serialnumber',
            'updated',
            'timestamp',
            'delete_url', 
        ]
