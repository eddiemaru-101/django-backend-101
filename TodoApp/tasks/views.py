from rest_framework import viewsets, status
from .models import Task
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .dto import TaskCreateRequestDTO, TaskResponseDTO
from drf_spectacular.utils import extend_schema


@extend_schema(
    request = TaskCreateRequestDTO,
    responses = TaskResponseDTO
)
@api_view(['POST'])
def create_task(request):
    dto = TaskCreateRequestDTO(request.data)
    task = Task.objects.create(
        title=dto.title,
        description=dto.description,
        completed=dto.completed
    )
    response_dto = TaskResponseDTO(task)
    return Response(response_dto.to_dict(), status=status.HTTP_201_CREATED)


@api_view(['GET'])
def get_task(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response({"error": "할 일이 존재하지 않습니다."}, status=404)

    response_dto = TaskResponseDTO(task)
    return Response(response_dto.to_dict(), status=200)


