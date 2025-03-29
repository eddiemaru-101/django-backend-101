from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer


# ViewSet을 사용한 Task에 대한 CRUD 처리
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer