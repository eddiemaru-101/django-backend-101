# TodoApp/urls.py
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),  # tasks 앱의 URL을 포함


    path('schema/', SpectacularAPIView.as_view(), name='schema'),  # 스키마 URL
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),  # Swagger UI
]