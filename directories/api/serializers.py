# from django.contrib.auth.models import User
from django.db import models

from rest_framework.serializers import (
        HyperlinkedIdentityField,
        ModelSerializer,
        SerializerMethodField,
        )

from directories.models import  PhoneNumber, Department, Faculty
# from users.api.serializers import UserDetailSerializer





#Creating an ApplyMedical
class PhoneNumberCreateUpdateSerializer(ModelSerializer):
    department  = models.ForeignKey(Department, default=1, on_delete = models.CASCADE)
    class Meta:
        model = PhoneNumber
        fields = [
            'department',
            'phone', 
        ]


apply_detail_url = HyperlinkedIdentityField(
        view_name='directories-api:detail',
        lookup_field='pk'#or primary key <pk>
    )

class FacultyDetailSerializer(ModelSerializer):

    class Meta:
        model = Faculty
        fields = [
            'id',
            'shortname',
            'fullname',
            'dean',
            'location',
            'lat',
            'lng',
            'timestamp',
            'updated',
            ]

class DepartmentDetailSerializer(ModelSerializer):
    faculty = FacultyDetailSerializer(read_only=True)
    class Meta:
        model = Department
        fields = [
         
            'id',
            'shortname',
            'fullname',
            'location',
            'chairman',
            'email',
            'lat',
            'lng',
            'timestamp',
            'updated',
            'faculty',
            ]


class PhoneNumberDetailSerializer(ModelSerializer):
    url        = apply_detail_url
    department = DepartmentDetailSerializer(read_only=True)

    class Meta:
        model = PhoneNumber
        fields = [
            'url',
            'id',
            'phone',
            'timestamp',
            'updated',
            'department',
        ]
    

class PhoneNumberListSerializer(ModelSerializer):
    url = apply_detail_url
    department = DepartmentDetailSerializer(read_only=True)
    delete_url = HyperlinkedIdentityField(
        view_name='directories-api:delete',
        lookup_field='pk'#or primary key <pk>
    )
    class Meta:
        model = PhoneNumber
        fields = [
            'url',
            'id',
            'phone',
            'timestamp',
            'updated',
            'delete_url', 
            'department',
        ]