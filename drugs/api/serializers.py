from rest_framework.serializers import (
        HyperlinkedIdentityField,
        ModelSerializer,
        SerializerMethodField,
        )

from django.contrib.auth.models import User
from django.db import models
from drugs.models import Drug
from users.api.serializers import UserDetailSerializer
  
#Creating an new
class DrugsCreateUpdateSerializer(ModelSerializer):
    user   = models.ForeignKey(User, default=1, on_delete = models.CASCADE)
    class Meta:
        model = Drug
        fields = [
            'user',
            'name',
            'status',
            'price',
        ]


new_detail_url = HyperlinkedIdentityField(
        view_name='drugs-api:detail',
        lookup_field='pk'#or primary key <pk>
    )

# Drug Details
class DrugsDetailSerializer(ModelSerializer):
    url    = new_detail_url
    user   = UserDetailSerializer(read_only=True)
    class Meta:
        model = Drug
        fields = [
            'url',
            'id',
            'user',
            'name',
            'status',
            'price',
            'timestamp',
        ]

# All Drugs List
class DrugsListSerializer(ModelSerializer):
    url = new_detail_url
    user = UserDetailSerializer(read_only=True)
    delete_url = HyperlinkedIdentityField(
        view_name='drugs-api:delete',
        lookup_field='pk'#or primary key <pk>
    )
    class Meta:
        model = Drug
        fields = [
            'url',
            'id',
            'user',
            'name',
            'status',
            'price',
            'timestamp',
            'delete_url', 
        ]
    
    # def get_user(self, obj):
    #     return str(obj.user.username)
