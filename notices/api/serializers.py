from rest_framework.serializers import (
        HyperlinkedIdentityField,
        ModelSerializer,
        SerializerMethodField,
        )

from django.contrib.auth.models import User
from django.db import models 
from notices.models import Notice
from users.api.serializers import UserDetailSerializer
  
#Creating an new
class NoticesCreateUpdateSerializer(ModelSerializer):
    user   = models.ForeignKey(User, default=1, on_delete = models.CASCADE)
    class Meta:
        model = Notice
        fields = [
            'user',
            'title',
            'content',
            'image',
            'image1',
        ]
    
    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None

        return image
    
    def get_image1(self, obj):
        try:
            image1 = obj.image1.url
        except:
            image1 = None

        return image1


new_detail_url = HyperlinkedIdentityField(
        view_name='notices-api:detail',
        lookup_field='pk'#or primary key <pk>
    )

# Notice Details
class NoticesDetailSerializer(ModelSerializer):
    url    = new_detail_url
    user   = UserDetailSerializer(read_only=True)
    class Meta:
        model = Notice
        fields = [
            'url',
            'id',
            'user',
            'title',
            'content',
            'image',
            'image1',
            'updated',
            'timestamp',
        ]

# All Notices List
class NoticesListSerializer(ModelSerializer):
    url = new_detail_url
    user = UserDetailSerializer(read_only=True)
    delete_url = HyperlinkedIdentityField(
        view_name='notices-api:delete',
        lookup_field='pk'#or primary key <pk>
    )
    class Meta:
        model = Notice
        fields = [
            'url',
            'id',
            'user',
            'title',
            'content',
            'image',
            'image1',
            'updated',
            'timestamp',
            'delete_url', 
        ]
    
    # def get_user(self, obj):
    #     return str(obj.user.username)
