from .models import Task
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .dto import TaskCreateRequestDTO, TaskResponseDTO
from drf_spectacular.utils import extend_schema
from .serializers import TaskCreateSerializer, TaskResponseSerializer
from TodoApp.constants import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
)

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
        return Response(response_serializer.data, status=HTTP_201_CREATED)
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@extend_schema(
    responses=TaskResponseSerializer
)
@api_view(['GET'])
def get_task(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response({"error": "할 일이 존재하지 않습니다."}, status=HTTP_404_NOT_FOUND)

    response_serializer = TaskResponseSerializer(task)
    return Response(response_serializer.data, status=HTTP_200_OK)
