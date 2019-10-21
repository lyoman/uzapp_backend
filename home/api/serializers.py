from rest_framework.serializers import (
        HyperlinkedIdentityField,
        ModelSerializer,
        SerializerMethodField,
        )

from django.contrib.auth.models import User
from django.db import models
from home.models import Home
from users.api.serializers import UserDetailSerializer
  
#Creating an new
class HomesCreateUpdateSerializer(ModelSerializer):
    user   = models.ForeignKey(User, default=1, on_delete = models.CASCADE)
    class Meta:
        model = Home
        fields = [
            'user',
            'title',
            'content',
            'banner',
            'banner1',
            'banner2',
            'banner3',
            'link_url'
        ]
    
    def get_image(self, obj):
        try:
            banner = obj.banner.url
        except:
            banner = None

        return banner
    
    def get_image1(self, obj):
        try:
            banner1 = obj.banner1.url
        except:
            banner1 = None

        return banner1


new_detail_url = HyperlinkedIdentityField(
        view_name='home-api:detail',
        lookup_field='pk'#or primary key <pk>
    )

# Home Details
class HomesDetailSerializer(ModelSerializer):
    url    = new_detail_url
    user   = UserDetailSerializer(read_only=True)
    class Meta:
        model = Home
        fields = [
            'url',
            'id',
            'user',
            'title',
            'content',
            'banner',
            'banner1',
            'banner2',
            'banner3',
            'link_url',
            'updated',
            'timestamp',
        ]

# All Homes List
class HomesListSerializer(ModelSerializer):
    url = new_detail_url
    user = UserDetailSerializer(read_only=True)
    delete_url = HyperlinkedIdentityField(
        view_name='home-api:delete',
        lookup_field='pk'#or primary key <pk>
    )
    class Meta:
        model = Home
        fields = [
            'url',
            'id',
            'user',
            'title',
            'content',
            'banner',
            'banner1',
            'banner2',
            'banner3',
            'link_url',
            'updated',
            'timestamp',
            'delete_url', 
        ]
    
    # def get_user(self, obj):
    #     return str(obj.user.username)
