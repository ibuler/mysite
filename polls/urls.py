from django.conf.urls import url

from . import views

app_name = "polls"

urlpatterns = [
    url('^$', views.index),
    url('^csv/$', views.down_csv),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]