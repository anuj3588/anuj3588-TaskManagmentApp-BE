from django.urls import path

from Task.Api.v1.task.views import TasksViews, TasksDetailsViews

urlpatterns = [
    path("tasks", TasksViews.as_view(), name="tasks"),
    path("tasks/<str:slug>", TasksDetailsViews.as_view(), name="task"),
]
