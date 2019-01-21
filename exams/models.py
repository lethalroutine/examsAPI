from django.db import models


class Exam(models.Model):
    owner = models.ForeignKey('auth.User', related_name='exams', on_delete=models.CASCADE)
    grade = models.IntegerField(null=True)
    students_name = models.CharField(max_length=30)


class ExamFile(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    file = models.FileField(upload_to='exams')
    file_name = models.CharField(max_length=255)


class Task(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    task_number = models.IntegerField()
    number_of_points = models.FloatField()
