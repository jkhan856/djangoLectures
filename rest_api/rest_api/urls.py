from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

urlpatterns = [
        url(r'^api_service/songs/', include('api_service.urls')),
        url(r'^admin/', admin.site.urls),
]
