# TodoApp/urls.py
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),  # tasks 앱의 URL을 포함

    # 스키마 URL
    path('schema/', SpectacularAPIView.as_view(), name='schema'), 
    # Swagger UI (HTML 문서 형식)
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),  
    # ReDoc UI (깔끔한 문서 형식)
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'), 

]