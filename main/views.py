import pickle
from typing import Any
from django.http import Http404
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from MarkLib.grader import Grader
from MarkLib import task as marklibtask
from CGTasks.graham.task import GrahamTask
from CGTasks.graham.grader import GrahamGrader


from .serializers import ModuleSerializer, TaskSerializer, UserSerializer, UniversityGroupSerializer
from main.models import Module, Task, UniversityGroup
from django.contrib.auth import get_user_model
User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class UniversityGroupViewSet(viewsets.ModelViewSet):
    queryset = UniversityGroup.objects.all()
    serializer_class = UniversityGroupSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


class TaskAPIView(APIView):
    grader: type = Grader
    task_class: type = marklibtask.Task

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get(self, request, id, formats=None):
        try:
            task = pickle.load(Task.objects.get(id=id).pickle_dump)
            assert isinstance(task, self.task_class)
        except (Task.DoesNotExist, AssertionError):
            raise Http404

        return Response(task.condition.dict())
    
    def post(self, request, id):
        try:
            task = pickle.load(Task.objects.get(id=id).pickle_dump)
        except Task.DoesNotExist:
            raise Http404
        
        correct_answers = task.answers
        student_answers = [
            type(answer)(**answer_data)
            for answer, answer_data
            in zip(correct_answers, request.data)
        ]
        return Response(self.grader.grade(correct_answers, student_answers))
    

class GrahamTaskAPIView(TaskAPIView):
    grader = GrahamGrader
    task_class = GrahamTask
