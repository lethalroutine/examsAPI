from django.http import Http404, HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from rest_framework import status, generics
from rest_framework.parsers import FileUploadParser
from exams.models import Exam, ExamFile, Task
from exams.serializers import ExamSerializer,TaskSerializer
from wsgiref.util import FileWrapper

import os


class ExamList(generics.ListAPIView):
    """
    View to list all sent exams
    """
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer


class ExamDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View to get the details of sent exam with possibility to update
    """
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer


class ExamCreate(generics.CreateAPIView):
    """
    View to create exam
    """
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer


class ExamFileDetail(APIView):
    """
    View to manage exam sheets
    """
    parser_classes = (FileUploadParser,)

    def get(self, request, pk):
        exam_file = ExamFile.objects.get(pk=pk)
        file_path = exam_file.file.name
        f = open('data/' + file_path, 'rb')
        resp = HttpResponse(FileWrapper(f), content_type='application/pdf')
        resp['Content-Disposition'] = 'attachment; filename=' + exam_file.file_name
        return resp

    def post(self, request, pk, format=None):

        if 'file' not in request.data:
            raise ParseError('Empty content')

        f = request.data['file']

        ExamFile(exam=Exam.objects.get(pk=pk),
                 file_name=f.name).file.save(f.name, f, save=True)
        return Response(status=status.HTTP_201_CREATED)

    def delete(self, request, pk, format=None):
        exam_file = ExamFile.objects.get(pk=pk)

        try:
            os.remove("data/" + exam_file.file.name)
        except:
            print('could not delete file ' + "data/" + exam_file.file.name)
        exam_file.file.delete(save=True)
        return Response(status=status.HTTP_204_NO_CONTENT)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView,
                 generics.CreateAPIView):
    """
    View to assign points to exam task
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
