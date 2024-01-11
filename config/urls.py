from django.contrib import admin
from django.urls import path, include

from config.views import (
    TaskListView,
    TaskCreateView,
    update_status_view,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    TaskUpdateView,
    TasklDeleteView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-view"),
    path("create_task/", TaskCreateView.as_view(), name="create-task"),
    path("update_task/<int:pk>", TaskUpdateView.as_view(), name="update-task"),
    path(
        "delete-task/<int:pk>",
        TasklDeleteView.as_view(),
        name="delete-task"
    ),


    path("tag_list/", TagListView.as_view(), name="tag-list"),
    path("tag_create/",
         TagCreateView.as_view(),
         name="tag-create"
         ),
    path("tag_update/<int:pk>/", TagUpdateView.as_view(), name="tag-update"),
    path("tag_delete/<int:pk>/", TagDeleteView.as_view(), name="tag-delete"),

    path(
        "<int:pk>/update-status/",
        update_status_view,
        name="task-status-update"
    ),
]

app_name = "config"
