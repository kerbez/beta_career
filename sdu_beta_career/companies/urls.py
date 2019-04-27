from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from . import views
from sdu_beta_career.companies.views import (
    company_list,
    company_detail,
    company_search,
    get_queryset,
    CompaniesSearchView)

app_name = "companies"

urlpatterns = [
    path('', view=company_list, name='company_list'),
    path('<int:pk>/', view=company_detail, name='company_detail'),
    # path('search', view=company_search, name='company_search'),
    path('search', CompaniesSearchView.as_view(), name='company_search'),

    path('result', view=get_queryset, name='get_queryset'),
]
