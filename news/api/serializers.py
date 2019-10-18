from rest_framework.serializers import (
        HyperlinkedIdentityField,
        ModelSerializer,
        SerializerMethodField,
        )

from django.contrib.auth.models import User
from django.db import models
from news.models import New, Reader
from users.api.serializers import UserDetailSerializer


reader_detail_url = HyperlinkedIdentityField(
        view_name='news-api:detail1',
        lookup_field='pk'#or primary key <pk>
    )


class ReaderDetailSerializer(ModelSerializer):
    url    = reader_detail_url
    class Meta:
        model = Reader
        fields = [
            'id',
            'url',
            'name',
            'updated',
            'timestamp',
        ]

class ReaderListSerializer(ModelSerializer):
    url = reader_detail_url
    UserDetailSerializer(read_only=True)
 
    class Meta:
        model = Reader
        fields = [
            'url',
            'id',
            'name',
            'updated',
            'timestamp', 
        ]
    


#Creating an new
class NewsCreateUpdateSerializer(ModelSerializer):
    user   = models.ForeignKey(User, default=1, on_delete = models.CASCADE)
    reader = models.ForeignKey(Reader, default=1, on_delete = models.CASCADE)
    class Meta:
        model = New
        fields = [
            'user',
            'reader',
            'title',
            'content',
            'image',
            'link_url',
        ]


new_detail_url = HyperlinkedIdentityField(
        view_name='news-api:detail',
        lookup_field='pk'#or primary key <pk>
    )

# New Details
class NewsDetailSerializer(ModelSerializer):
    url    = new_detail_url
    user   = UserDetailSerializer(read_only=True)
    reader = ReaderDetailSerializer(read_only=True)
    image  = SerializerMethodField()
    class Meta:
        model = New
        fields = [
            'url',
            'id',
            'user',
            'reader',
            'title',
            'content',
            'news_date',
            'news_time',
            'timestamp',
            'image',
            'link_url',
        ]
    
    # def get_user(self, obj):
    #     return str(obj.user.username)

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        
        return image

# All News List
class NewsListSerializer(ModelSerializer):
    url = new_detail_url
    reader = ReaderDetailSerializer(read_only=True)
    UserDetailSerializer(read_only=True)
    delete_url = HyperlinkedIdentityField(
        view_name='news-api:delete',
        lookup_field='pk'#or primary key <pk>
    )
    class Meta:
        model = New
        fields = [
            'url',
            'id',
            'user',
            'reader',
            'title',
            'content',
            'news_date',
            'news_time',
            'timestamp',
            'image',
            'link_url',
            'delete_url', 
        ]
    
    # def get_user(self, obj):
    #     return str(obj.user.username)
