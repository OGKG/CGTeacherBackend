from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ModuleSerializer, ModuleTasksSerializer, TaskSerializer, UserSerializer, UniversityGroupSerializer
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
