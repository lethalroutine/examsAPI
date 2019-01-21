from django.urls import path
from . import views

urlpatterns = [
    path('exams/', views.ExamList.as_view()),
    path('exams/<int:pk>/', views.ExamDetail.as_view()),
    path('exams/files/update/<int:pk>', views.ExamFileUpdate.as_view()),
    path('exams/files/download/<int:pk>/', views.ExamFileDownload.as_view()),
    path('exams/files/upload', views.ExamFileUpload.as_view()),
    path('exams/create', views.ExamCreate.as_view()),
    path('exams/tasks/<int:pk>', views.TaskDetail.as_view()),
    path('exams/tasks/', views.TaskList.as_view()),
    path('exams/users/', views.UserList.as_view()),
    path('exams/users/<int:pk>', views.UserDetail.as_view()),
]
