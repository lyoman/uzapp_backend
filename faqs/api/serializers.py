from rest_framework.serializers import (
        HyperlinkedIdentityField,
        ModelSerializer,
        SerializerMethodField,
        )

from django.contrib.auth.models import User
from django.db import models
from faqs.models import Faq
from users.api.serializers import UserDetailSerializer
  
#Creating an new
class FaqsCreateUpdateSerializer(ModelSerializer):
    user   = models.ForeignKey(User, default=1, on_delete = models.CASCADE)
    class Meta:
        model = Faq
        fields = [
            'user',
            'name',
            'question',
            'answer',
            'link'
        ]


new_detail_url = HyperlinkedIdentityField(
        view_name='faqs-api:detail',
        lookup_field='pk'#or primary key <pk>
    )

# Faq Details
class FaqsDetailSerializer(ModelSerializer):
    url    = new_detail_url
    user   = UserDetailSerializer(read_only=True)
    class Meta:
        model = Faq
        fields = [
            'url',
            'id',
            'user',
            'name',
            'question',
            'answer',
            'link',
            'timestamp',
        ]

# All Faqs List
class FaqsListSerializer(ModelSerializer):
    url = new_detail_url
    user = UserDetailSerializer(read_only=True)
    delete_url = HyperlinkedIdentityField(
        view_name='faqs-api:delete',
        lookup_field='pk'#or primary key <pk>
    )
    class Meta:
        model = Faq
        fields = [
            'url',
            'id',
            'user',
            'name',
            'question',
            'answer',
            'link',
            'timestamp',
            'delete_url', 
        ]
    
    # def get_user(self, obj):
    #     return str(obj.user.username)
