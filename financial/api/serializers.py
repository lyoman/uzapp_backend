from rest_framework.serializers import (
        HyperlinkedIdentityField,
        ModelSerializer,
        SerializerMethodField,
        )

from django.db import models
from django.contrib.auth.models import User
from financial.models import FinancialStatement
from users.api.serializers import UserDetailSerializer
    

#Creating an new
class FinancialStatementCreateUpdateSerializer(ModelSerializer):
    user        = models.ForeignKey(User, default=1, on_delete = models.CASCADE)
    class Meta:
        model = FinancialStatement
        fields = [
            'user',
            'description',
            'date',
            'debit',
            'credit',
            'closing_balance',
        ]


new_detail_url = HyperlinkedIdentityField(
        view_name='financial-api:detail',
        lookup_field='pk'#or primary key <pk>
    )

# FinancialStatement Details
class FinancialStatementDetailSerializer(ModelSerializer):
    user   = UserDetailSerializer(read_only=True)
    url    = new_detail_url
    class Meta:
        model = FinancialStatement
        fields = [
            'url',
            'id',
            'user',
            'description',
            'date',
            'debit',
            'credit',
            'closing_balance',
            'updated',
            'timestamp',
        ]

# All FinancialStatement List
class FinancialStatementListSerializer(ModelSerializer):
    user   = UserDetailSerializer(read_only=True)
    url = new_detail_url
    delete_url = HyperlinkedIdentityField(
        view_name='financial-api:delete',
        lookup_field='pk'#or primary key <pk>
    )
    class Meta:
        model = FinancialStatement
        fields = [
            'url',
            'id',
            'user',
            'description',
            'date',
            'debit',
            'credit',
            'closing_balance',
            'updated',
            'timestamp',
            'delete_url', 
        ]
