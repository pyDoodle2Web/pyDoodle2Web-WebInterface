
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('upload/', views.upload, name='upload'),
    # path('generate/', views.generate, name='generate'),
    path('downloadSource/', views.downloadSource, name='downloadSource'),
    path('readImage/', views.readImage, name='readImage'),
    path('generate/', views.generate, name='generate'),
    path('generatedSite/', views.generatedSite, name='generatedSite')

] 
