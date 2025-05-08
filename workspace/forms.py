from django.forms import forms

from workspace.models import Task, Tag


class TaskCreationForm(forms.Form):
    class Meta:
        model = Task
        fields = ("name", "content", "deadline", "tag",)


class TaskUpdateForm(forms.Form):
    class Meta:
        model = Task
        fields = ("name", "content", "deadline", "tag",)


#---------------------------------------------Tags

class TagCreationForm(forms.Form):
    class Meta:
        model = Tag
        fields = ("name",)


class TagUpdateForm(forms.Form):
    class Meta:
        model = Tag
        fields = ("name",)