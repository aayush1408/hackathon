from django.conf.urls import url, include
from .views import *


urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'signup/$', signup, name='signup'),
    url(r'^logout/$',logout, name='logout'),
    url(r'^log_in/$', log_in, name='log_in'),
    url(r'^auth_check/$', auth_check, name='check'),
    url(r'change_password/$', change_password, name='change_password'),

    url(r'^captcha/', include('captcha.urls')),

]
