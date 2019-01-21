from django.contrib import admin
from .models import ExamFile, Exam, Task

# Register your models here.
admin.site.register((Exam, ExamFile, Task))
