from django.conf.urls import url
from django.contrib import admin

from .views import (
    FinancialStatementCreateAPIView,
    FinancialStatementListAPIView,
    FinancialStatementDetailAPIView,
    FinancialStatementUpdateAPIView,
    FinancialStatementDeleteAPIView,
	)

urlpatterns = [
    url(r'^$', FinancialStatementListAPIView.as_view(), name='financial'),
    url(r'^(?P<pk>[\d]+)/$', FinancialStatementDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>[\d]+)/delete/$', FinancialStatementDeleteAPIView.as_view(), name="delete"),
    url(r'^(?P<pk>[\d]+)/edit/$', FinancialStatementUpdateAPIView.as_view(), name='update'),
    url(r'^register/$', FinancialStatementCreateAPIView.as_view(), name="create"),
]