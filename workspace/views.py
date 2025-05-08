from django.shortcuts import render
from django.views import generic

from workspace.models import Task


# Create your views here.
class TasksListView(generic.ListView):
    model = Task
    template_name = "workspace/tasks-list.html"
    context_object_name = "tasks"

