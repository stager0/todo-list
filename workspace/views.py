

from django.http import HttpResponseRedirect, HttpRequest
from django.urls import reverse, reverse_lazy
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
        return queryset.order_by("status").order_by("created_at")

    def post(self, request: HttpRequest, *args, **kwargs):
        action = self.request.POST.get("action")

        if action == "Done":
            Task.objects.filter(pk=self.request.POST.get("pk")).update(status=True)

        if action == "Undo":
            Task.objects.filter(pk=self.request.POST.get("pk")).update(status=False)

        return HttpResponseRedirect(self.request.path)

    def get_context_data(
        self, *, object_list = ..., **kwargs
    ):
        context = super().get_context_data(**kwargs)
        context["count_of_tasks"] = Task.objects.filter(status=False).count()
        return context


class TasksListCreateView(generic.CreateView):
    model = Task
    template_name = "workspace/task-create.html"
    form_class = TaskCreationForm
    success_url = reverse_lazy("workspace:tasks-list")


class TasksListUpdateView(generic.UpdateView):
    model = Task
    template_name = "workspace/task-update.html"
    form_class = TaskUpdateForm
    success_url = reverse_lazy("workspace:tasks-list")


class TasksListDeleteView(generic.DeleteView):
    model = Task
    template_name = "workspace/task-confirm-delete.html"
    success_url = reverse_lazy("workspace:tasks-list")


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
    success_url = reverse_lazy("workspace:tags-list")


class TagsListUpdateView(generic.UpdateView):
    model = Tag
    template_name = "workspace/tag-update.html"
    form_class = TagUpdateForm
    success_url = reverse_lazy("workspace:tags-list")


class TagsListDeleteView(generic.DeleteView):
    model = Tag
    template_name = "workspace/tag-confirm-delete.html"
    success_url = reverse_lazy("workspace:tags-list")

