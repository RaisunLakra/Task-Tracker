from django.urls import path

from .views import tasks, add_task, delete_task

app_name = 'app'

urlpatterns = [
    path('', tasks, name='tasks'),
    path('add-task/',add_task, name='add_task'),
    path('delete-task/<int:task_id>/', delete_task, name='delete_task')
]