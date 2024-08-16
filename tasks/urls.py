from django.urls import path
from .views import TaskListCreateView, TaskDetailView
from rest_framework import routers

app_name = 'tasks'

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
]