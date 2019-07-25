from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^powerBtn/$', views.powerBtn, name='powerBtn'),
    url(r'^timer/[0-9]{2}/[0-9]{2}/[0-9]{2}/$', views.timer, name='timer'),
]
