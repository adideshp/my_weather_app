from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^city/$', views.get_city, name='get_city'),
    url(r'^weather/$', views.get_weather, name='get_weather'),
]