from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    url(r'^$', views.SchoolListView.as_view(), name = 'list'),
    url(r'^(?P<pk>\d+)/$', views.SchoolDetailsView.as_view(), name = 'detail'),
    url(r'^create/$', views.CreateSchoolView.as_view(), name = 'create'),
    url(r'^update/(?P<pk>\d+)/$', views.UpdateSchoolView.as_view(), name = 'update'),
    url(r'^delete/(?P<pk>\d+)/$', views.DeleteSchoolView.as_view(), name = 'delete')
]
