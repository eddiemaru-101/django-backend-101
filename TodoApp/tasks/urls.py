# tasks/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

# DefaultRouter를 사용하여 ViewSet을 자동으로 URL에 매핑
router = DefaultRouter()
router.register(r'tasks', TaskViewSet)  # 'tasks' URL과 TaskViewSet 연결

urlpatterns = [
    path('api/', include(router.urls)),  # ViewSet을 위한 URL을 api/ 아래로 등록
]