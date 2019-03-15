from django.conf.urls import url
from django.conf.urls import include
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^other/', views.other, name ='other'),
    url(r'^relative/', views.relative, name = 'relative')
]
