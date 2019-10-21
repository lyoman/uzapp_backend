from rest_framework.serializers import (
        HyperlinkedIdentityField,
        ModelSerializer,
        SerializerMethodField,
        )

from django.contrib.auth.models import User
from django.db import models
from lostandfound.models import Lost
from users.api.serializers import UserDetailSerializer
  
#Creating an new
class LostsCreateUpdateSerializer(ModelSerializer):
    user   = models.ForeignKey(User, default=1, on_delete = models.CASCADE)
    class Meta:
        model = Lost
        fields = [
            'user',
            'name',
            'contact',
            'place',
            'image',
        ]


new_detail_url = HyperlinkedIdentityField(
        view_name='lostandfound-api:detail',
        lookup_field='pk'#or primary key <pk>
    )

# Lost Details
class LostsDetailSerializer(ModelSerializer):
    url    = new_detail_url
    user   = UserDetailSerializer(read_only=True)
    class Meta:
        model = Lost
        fields = [
            'url',
            'id',
            'user',
            'name',
            'contact',
            'place',
            'image',
            'updated',
            'timestamp',
        ]
    
    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None

        return image

# All Losts List
class LostsListSerializer(ModelSerializer):
    url = new_detail_url
    user = UserDetailSerializer(read_only=True)
    delete_url = HyperlinkedIdentityField(
        view_name='lostandfound-api:delete',
        lookup_field='pk'#or primary key <pk>
    )
    class Meta:
        model = Lost
        fields = [
            'url',
            'id',
            'user',
            'name',
            'contact',
            'place',
            'image',
            'updated',
            'timestamp',
            'delete_url', 
        ]
    
    # def get_user(self, obj):
    #     return str(obj.user.username)
