from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tasks/', views.TaskListCreate.as_view()),
    path('api/tasks/<int:pk>', views.TaskDetailUpdateDelete.as_view())
]
