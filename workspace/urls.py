from django.urls import path

from workspace.views import TasksListView, TasksListCreateView, TasksListUpdateView, TasksListDeleteView, \
    TagsListView, TagsListCreate, TagsListUpdateView, TagsListDeleteView

app_name="workspace"

urlpatterns = [
    path("tasks-list/", TasksListView.as_view(), name="tasks-list"),
    path("tasks-list-create/", TasksListCreateView.as_view(), name="task-create"),
    path("tasks-list/<int:pk>/update/", TasksListUpdateView.as_view(), name="task-update"),
    path("tasks-list/<int:pk>/delete/", TasksListDeleteView.as_view(), name="task-delete"),

    path("tags-list/", TagsListView.as_view(), name="tags-list"),
    path("tags-list/create/", TagsListCreate.as_view(), name="tags-list-create"),
    path("tags-list/<int:pk>/update/", TagsListUpdateView.as_view(), name="tag-update"),
    path("tags-list/<int:pk>/delete/", TagsListDeleteView.as_view(), name="tag-delete"),
]