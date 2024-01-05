from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic

from config.models import Task, Tag


# Create your views here.

class TaskListView(generic.ListView):
    model = Task
    fields = "__all__"
    queryset = Task.objects.prefetch_related("tags")


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    template_name = "config/task_form.html"
    success_url = reverse_lazy("config:task-view")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("config:task-view")


class TasklDeleteView(generic.DeleteView):
    model = Task
    fields = "__all__"
    template_name = "config/task_confirm_delete.html"
    success_url = reverse_lazy("config:task-view")


class TagListView(generic.ListView):
    model = Tag
    field = "__all__"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("config:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("config:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    fields = "__all__"
    template_name = "config/tag_confirm_delete.html"
    success_url = reverse_lazy("config:tag-list")


def update_status_view(request, pk):
    task = Task.objects.get(id=pk)
    task.status = not task.status
    task.save()

    return HttpResponseRedirect(reverse("config:task-view"))
