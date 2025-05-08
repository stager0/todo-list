from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=210, null=True, blank=True)
    deadline = models.DateField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
