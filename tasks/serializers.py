from rest_framework import serializers
from .models import Task, Subtask, Team, Tag, Comment


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = "__all__"


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"



