from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from django.conf.urls import url
urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path('',include('projekt_as.urls')),
    re_path('uzytkownicy/', include('django.contrib.auth.urls')),
    re_path('uzytkownicy/', include('uzytkownicy.urls'))
]
