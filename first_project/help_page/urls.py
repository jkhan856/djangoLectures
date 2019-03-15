from django.conf.urls import url
from help_page import views

urlpatterns = [
    url(r'^$',views.help_page, name = 'help_page'),
]
