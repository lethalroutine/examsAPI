from django.contrib import admin
from . models import ExamFile, Owner, Exam, Task

# Register your models here.
admin.site.register((Exam, ExamFile, Owner, Task))
