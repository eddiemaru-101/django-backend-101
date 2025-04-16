# tasks/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path('tasks/', views.create_task, name='create-task'),           # POST 요청
    path('tasks/<int:pk>/', views.get_task, name='get-task'),        # GET 요청
]