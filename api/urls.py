from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.fetch_current_data, name='index'),
    path('<str:symbol>/', views.history, name='history'),
]