
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('upload/', views.upload, name='upload'),
    path('generated/', views.generated, name='generated'),
    path('downloadSource/', views.downloadSource, name='downloadSource')
]
