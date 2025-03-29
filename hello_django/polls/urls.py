from django.urls import path
from . import views

app_name = "pollsss"

# name은 html에서 path설정할때 사용  "{% url "detail" q.id  %}"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>', views.detail, name='detail'),
    path('some_url/', views.some_url),
]