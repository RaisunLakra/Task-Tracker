from django.urls import path

from . import views

app_name = 'app'

urlpatterns = [
    path('tasks/', views.tasks, name='tasks'),
]