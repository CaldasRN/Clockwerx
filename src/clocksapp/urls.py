from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.powerBtn, name='powerBtn'),
#    url(r'^$', views.timer, name='timer'),
]
