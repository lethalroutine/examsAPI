from django.urls import path
from exams import views

urlpatterns = [
    path('exams/', views.ExamList.as_view()),
    path('exams/<int:pk>/', views.ExamDetail.as_view()),
    path('exams/files/<int:pk>/', views.ExamFileDetail.as_view()),
]