from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from CGMark.tasks.graham import GrahamTask
from .serializers import ModuleSerializer, TaskSerializer, UserSerializer, UniversityGroupSerializer
from main.models import Module, Task, UniversityGroup
from CGMark.base.models.condition import PointListCondition
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


class GrahamTaskAPIView(APIView):
    def __init__(self):
        condition = PointListCondition(point_list=[Point(x=7, y=0), Point(x=3, y=3), Point(x=0, y=0)])
        self.task = GrahamTask(condition=condition)
    
    def get(self, request, formats=None):
        return Response(self.task.condition.dict())
