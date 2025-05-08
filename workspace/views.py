from django.shortcuts import render
from django.views import generic

from workspace.models import Task


# Create your views here.
class TasksListView(generic.ListView):
    model = Task
    template_name = "workspace/tasks-list.html"
    context_object_name = "tasks"


class TasksListCreateView(generic.CreateView):
    pass


class TaskListDetailView(generic.DetailView):
    pass


class TasksListUpdateView(generic.UpdateView):
    pass


class TasksListDeleteView(generic.DeleteView):
    pass


class TaskIsDoneView(generic.View):
    pass


#--------------------------TAGS------------------

class TagsListView(generic.ListView):
    pass


class TagsListCreate(generic.CreateView):
    pass


class TagsListDetailView(generic.DetailView):
    pass


class TagsListUpdateView(generic.UpdateView):
    pass


class TagsListDeleteView(generic.DeleteView):
    pass

