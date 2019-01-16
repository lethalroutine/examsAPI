from django.http import Http404, HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from rest_framework import status
from rest_framework.parsers import FileUploadParser
from exams.models import Exam, ExamFile, Task
from exams.serializers import ExamSerializer,TaskSerializer
from wsgiref.util import FileWrapper
import os


class ExamList(APIView):
    """
    View to list all sent exams
    """
    def get(self, request, format=None):
        exams = Exam.objects.all()
        serializer = ExamSerializer(exams, many=True)
        return Response(serializer.data)


class ExamDetail(APIView):
    """
    View to get the details of sent exam with possibility to update
    """
    def get_object(self, pk):
        try:
            return Exam.objects.get(pk=pk)
        except Exam.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        exam = Exam.objects.get(pk=pk)
        serializer = ExamSerializer(exam)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        exam = self.get_object(pk=pk)
        serializer = ExamSerializer(exam, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExamCreate(APIView):
    """
    View to create exam
    """
    def post(self, request):
        serializer = ExamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



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


class TaskDetail(APIView):
    """
    View to assign points to exam task
    """
    def get_object(self, pk):
        try:
            return Exam.objects.get(pk=pk)
        except Exam.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        if len(Task.objects.filter(pk=pk)) == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        task = Task.objects.get(pk=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def post(self, request, pk):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        task = self.get_object(pk=pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
