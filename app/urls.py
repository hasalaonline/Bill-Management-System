from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('main', views.main, name='main'),
    path('ceb', views.ceb, name='ceb'),
    path('nwsdb', views.nwsdb, name='nwsdb'),    
]