from .models import Task
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .dto import TaskCreateRequestDTO, TaskResponseDTO
from drf_spectacular.utils import extend_schema
from .serializers import TaskCreateSerializer, TaskResponseSerializer
from rest_framework.exceptions import APIException
from django.shortcuts import get_object_or_404
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
    serializer.is_valid(raise_exception=True)

    try:
        task = Task.objects.create(**serializer.validated_data)
    except Exception as e:
        raise APIException(f"할 일 생성 중 오류 발생: {str(e)}")

    response_serializer = TaskResponseSerializer(task)
    return Response(response_serializer.data, status=HTTP_201_CREATED)


@extend_schema(
    responses=TaskResponseSerializer
)
@api_view(['GET'])
def get_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    response_serializer = TaskResponseSerializer(task)
    return Response(response_serializer.data, status=HTTP_200_OK)
