
from rest_framework import serializers
from .models import Task

class TaskCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    completed = serializers.BooleanField(default=False)

class TaskResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed']