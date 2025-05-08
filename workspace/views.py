from django.shortcuts import render
from django.views import generic

from workspace.forms import TagCreationForm, TagUpdateForm, TaskCreationForm, TaskUpdateForm
from workspace.models import Task, Tag


# Create your views here.
class TasksListView(generic.ListView):
    model = Task
    template_name = "workspace/tasks-list.html"
    context_object_name = "tasks"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by("status")


class TasksListCreateView(generic.CreateView):
    model = Task
    template_name = "workspace/task-create.html"
    form_class = TaskCreationForm


class TaskListDetailView(generic.DetailView):
    model = Task
    template_name = "workspace/task-detail.html"

    def get_queryset(self):
        return Task.objects.filter(pk=self.request.GET.get("pk"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task"] = self.get_object()
        return context


class TasksListUpdateView(generic.UpdateView):
    model = Task
    template_name = "workspace/task-update.html"
    form_class = TaskUpdateForm


class TasksListDeleteView(generic.DeleteView):
    model = Task
    template_name = "workspace/task-delete.html"


class TaskIsDoneView(generic.View):
    def save(self):
        pass


#--------------------------TAGS------------------

class TagsListView(generic.ListView):
    model = Tag
    template_name = "workspace/tags-list.html"
    context_object_name = "tags"

    def get_queryset(self):
        return Tag.objects.order_by("name")


class TagsListCreate(generic.CreateView):
    model = Tag
    template_name = "workspace/tag-create.html"
    form_class = TagCreationForm


class TagsListDetailView(generic.DetailView):
    model = Tag
    template_name = "workspace/tag-detail.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return Tag.objects.filter(pk=self.request.GET.get("pk"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag"] = self.get_object()
        return context


class TagsListUpdateView(generic.UpdateView):
    model = Tag
    template_name = "workspace/tag-update.html"
    form_class = TagUpdateForm


class TagsListDeleteView(generic.DeleteView):
    model = Tag
    template_name = "workspace/tag-delete.html"

