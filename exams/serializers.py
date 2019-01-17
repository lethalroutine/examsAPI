from rest_framework import serializers
from exams.models import Exam, Owner, Task, ExamFile


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ('id', 'owner', 'grade', 'students_name')


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ('id', 'username')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'exam', 'task_number', 'number_of_points')


class ExamFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamFile
        fields = ('id', 'exam', 'file', 'file_name')
