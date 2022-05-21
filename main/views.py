from typing import Any
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from CGMark.base.models.graham import GrahamPoint, GrahamPointList, GrahamTable
from CGMark.mark.grader import Grader
from CGMark.mark.graders.graham import GrahamGrader

from CGMark.tasks.graham import GrahamTask
from .serializers import ModuleSerializer, TaskSerializer, UserSerializer, UniversityGroupSerializer
from main.models import Module, Task, UniversityGroup
from CGMark.base.models.condition import Condition, PointListCondition
from CGMark.base.models.base import Point
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
    task_class: type = Task
    condition_class: type = Condition
    condition_kwargs: dict[str, Any] = dict()

    def __init__(self, **kwargs):
        condition = self.condition_class(**self.condition_kwargs)
        self.task = self.task_class(condition=condition)
        super().__init__(**kwargs)  

    def get(self, request, formats=None):
        return Response(self.task.condition.dict())
    
    def post(self, request):
        correct_answers = self.task.answers
        student_answers = [
            type(answer)(**answer_data)
            for answer, answer_data 
            in zip(correct_answers, request.data)
        ]
        return Response(self.grader.grade(correct_answers, student_answers))
    

class GrahamTaskAPIView(TaskAPIView):
    grader: type = GrahamGrader
    task_class: type = GrahamTask
    condition_class: type = PointListCondition
    condition_kwargs: dict[str, Any] = {"point_list": [Point(x=7, y=0), Point(x=3, y=3), Point(x=0, y=0)]}
