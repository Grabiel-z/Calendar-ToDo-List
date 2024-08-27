from django.db import models
from users.models import User


class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User, related_name="teams")


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    responsible = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="tasks_responsible"
    )
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="tasks_created"
    )
    due_date = models.DateField(null=True, blank=True)
    completed_date = models.DateField(null=True, blank=True)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="tasks", null=True, blank=True
    )


class Subtask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="subtasks")
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)
    completed_date = models.DateField(null=True, blank=True)


class Tag(models.Model):
    title = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    tasks = models.ManyToManyField(Task, related_name="tags")


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
