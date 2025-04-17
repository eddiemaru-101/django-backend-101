from rest_framework import viewsets, status
from .models import Task
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .dto import TaskCreateRequestDTO, TaskResponseDTO
from drf_spectacular.utils import extend_schema
from .serializers import TaskCreateSerializer, TaskResponseSerializer

@extend_schema(
    request=TaskCreateSerializer,
    responses=TaskResponseSerializer
)
@api_view(['POST'])
def create_task(request):
    serializer = TaskCreateSerializer(data=request.data)
    if serializer.is_valid():
        task = Task.objects.create(**serializer.validated_data)
        response_serializer = TaskResponseSerializer(task)
        return Response(response_serializer.data, status=201)
    return Response(serializer.errors, status=400)


@extend_schema(
    responses=TaskResponseSerializer
)
@api_view(['GET'])
def get_task(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response({"error": "할 일이 존재하지 않습니다."}, status=404)

    response_serializer = TaskResponseSerializer(task)
    return Response(response_serializer.data, status=200)
