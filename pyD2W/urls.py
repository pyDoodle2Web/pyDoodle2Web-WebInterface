
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('upload/', views.home, name='upload'),
    path('readImage/', views.readImage, name='readImage'),
    path('generate/', views.generate, name='generate'),
    path('generatedSite/', views.home, name='generatedSite'),
    path('downloadSource/', views.downloadSource, name='downloadSource'),
] 
