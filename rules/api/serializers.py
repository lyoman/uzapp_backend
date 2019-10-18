from rest_framework.serializers import (
        HyperlinkedIdentityField,
        ModelSerializer,
        SerializerMethodField,
        )

from django.contrib.auth.models import User
from django.db import models
from rules.models import Rule
from users.api.serializers import UserDetailSerializer
  
#Creating an new
class RulesCreateUpdateSerializer(ModelSerializer):
    user   = models.ForeignKey(User, default=1, on_delete = models.CASCADE)
    class Meta:
        model = Rule
        fields = [
            'user',
            'name',
            'category',
            'details'
        ]


new_detail_url = HyperlinkedIdentityField(
        view_name='rules-api:detail',
        lookup_field='pk'#or primary key <pk>
    )

# Rule Details
class RulesDetailSerializer(ModelSerializer):
    url    = new_detail_url
    user   = UserDetailSerializer(read_only=True)
    class Meta:
        model = Rule
        fields = [
            'url',
            'id',
            'user',
            'name',
            'details',
            'category',
            'timestamp',
        ]

# All Rules List
class RulesListSerializer(ModelSerializer):
    url = new_detail_url
    user = UserDetailSerializer(read_only=True)
    delete_url = HyperlinkedIdentityField(
        view_name='rules-api:delete',
        lookup_field='pk'#or primary key <pk>
    )
    class Meta:
        model = Rule
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
    
    # def get_user(self, obj):
    #     return str(obj.user.username)
