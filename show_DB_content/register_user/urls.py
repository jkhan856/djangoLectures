from django.conf.urls import url
from register_user import views

urlpatterns = [
    url(r'^$',views.index, name = 'index'),
]
