from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^powerBtn/$', views.powerBtn),
    url(r'^timer/$', views.timer),
]
