from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^powerBtn/', views.powerBtn, name='powerBtn'),
    url(r'^timer/$', views.timer, name='timer'),
    url(r'^sync/$', views.sync, name='sync'),
    url(r'^milTime/$', views.milTime, name='milTime'),
    url(r'^dim/$', views.dim, name='dim'),
    url(r'^meshctl/$', views.meshctl, name='meshctl'),
#    url(r'^$', views.clocks, name='clocks'),
#    url(r'^api/timer/$', views.TimerListCreate.as_view() ),
]
