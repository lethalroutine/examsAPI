from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import generics, permissions
from .models import Exam, ExamFile, Task
from django.contrib.auth.models import User
from .serializers import ExamSerializer, TaskSerializer, ExamFileSerializer, UserSerializer
from wsgiref.util import FileWrapper
from .permissions import IsOwnerOrReadOnly, IsOwnerOrReadOnlyFile


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
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)


class ExamCreate(generics.CreateAPIView):
    """
    View to create exam
    """
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ExamFileUpload(generics.CreateAPIView):
    """"
    View to upload exam sheets
    """
    queryset = ExamFile.objects.all()
    serializer_class = ExamFileSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsOwnerOrReadOnlyFile)


class ExamFileDownload(APIView):
    """
    View to download exam sheets
    """
    queryset = ExamFile.objects.all()
    serializer_class = ExamFileSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk):
        exam_file = ExamFile.objects.get(pk=pk)
        file_path = exam_file.file.name
        f = open('data/' + file_path, 'rb')
        resp = HttpResponse(FileWrapper(f), content_type='application/pdf')
        resp['Content-Disposition'] = 'attachment; filename=' + exam_file.file_name
        return resp


class ExamFileUpdate(generics.UpdateAPIView,
                     generics.DestroyAPIView):
    """
    View to update or delete exam sheets
    """
    queryset = ExamFile.objects.all()
    serializer_class = ExamFileSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsOwnerOrReadOnlyFile)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView,
                 generics.CreateAPIView):
    """
    View to assign points to exam task
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class TaskList(generics.ListAPIView):
    """
    View to list all tasks
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
