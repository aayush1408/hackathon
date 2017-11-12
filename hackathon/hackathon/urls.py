from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('hack.urls')),
    url(r'^password_reset/', include('password_reset.urls')),

]
