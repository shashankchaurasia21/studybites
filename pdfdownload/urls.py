from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.pdfhome,name='home'),
    path('pdfmath', views.pdfmath, name='math'),
]