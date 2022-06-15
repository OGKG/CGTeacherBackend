from rest_framework import serializers
from main.models import Module, Student, Task, UniversityGroup


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('username', 'group')


class UniversityGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityGroup
        fields = ('name',)


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'pickle_dump')


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ('name', 'description', 'tasks')


class ModuleTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('name', 'description', 'max_score')
