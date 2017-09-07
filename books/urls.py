"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from django.http import HttpResponse
from django.shortcuts import render
from . import views
from . import api

app_name = "books"

router = DefaultRouter()
router.register(r'api/authors', api.AuthorViewSet)

urlpatterns = [
    url(r'^publisher/$', views.PublisherList.as_view(), name="publisher-list"),
    url(r'^publisher/(?P<pk>[0-9]+)/$', views.PublisherDetail.as_view(), name="publisher-detail"),
    url(r'^publisher/add/$', views.publisher_add),
    url(r'^publisher/([0-9]+)/update/$', views.publisher_update),
    url(r'^author/$', views.AuthorList.as_view(), name="author-list"),
    # url(r'^api/author/$', api.AuthorListApi.as_view(), name="api-author-list"),
    # url(r'^api/author/(?P<pk>[0-9]+)/$', api.AuthorDetailApi.as_view(), name="api-author-detail"),
    url(r'^author/add/$', views.AuthorCreate.as_view(), name="author-create"),
    url(r'^author/(?P<pk>[0-9]+)/update/$', views.AuthorUpdate.as_view(), name="author-update"),
    url(r'^author/(?P<pk>[0-9]+)/delete/$', views.AuthorDelete.as_view(), name="author-delete"),
]

urlpatterns += [
    url(r'^', include(router.urls)),
]

