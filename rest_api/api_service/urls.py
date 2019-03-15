from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from api_service import views

app_name = 'api_service'

urlpatterns = [
    url(r'^$', views.PlayListCreateView.as_view(), name = 'post-create'),
    url(r'getAll/$', views.PlayListAllView.as_view(), name = 'get-list'),
    url(r'^(?P<pk>\d+)/$', views.PlayListRudView.as_view(), name = 'post-rud'),
]
