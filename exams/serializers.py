from rest_framework import serializers
from .models import Exam, Task, ExamFile
from django.contrib.auth.models import User


class ExamSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Exam
        fields = ('id', 'grade', 'students_name', 'owner')


class UserSerializer(serializers.ModelSerializer):
    exams = serializers.PrimaryKeyRelatedField(many=True, queryset=Exam.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'exams')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'exam', 'task_number', 'number_of_points')


class ExamFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamFile
        fields = ('id', 'exam', 'file', 'file_name')
