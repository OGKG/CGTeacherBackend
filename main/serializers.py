from rest_framework import serializers
from main.models import Student, UniversityGroup


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('username', 'group')

class UniversityGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityGroup
        fields = ('name',)
