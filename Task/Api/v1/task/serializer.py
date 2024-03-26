from rest_framework import serializers

from Task.models import Tasks


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ["id", "title", "description", "status", "due_date", "slug"]
        read_only_fields = ["id"]


class TasksUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ["id", "title", "description", "status", "due_date", "slug"]
        read_only_fields = ["id", "title", "description", "due_date", "slug"]

