from django import forms

from workspace.models import Task, Tag


class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("content", "deadline", "tag",)


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("content", "deadline", "tag",)


#---------------------------------------------Tags

class TagCreationForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ("name",)


class TagUpdateForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ("name",)
