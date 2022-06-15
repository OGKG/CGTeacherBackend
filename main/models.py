from django.db import models
from django.db.models import Sum, CASCADE
from django.contrib.auth.models import AbstractUser


class UniversityGroup(models.Model):
    '''A group of students'''
    name = models.CharField('Group Name', max_length=10, null=False)

    def __str__(self):
        return self.name
        
    def __repr__(self):
        return self.name


class Student(AbstractUser):
    '''Student model, an extension of Django User'''
    group = models.ForeignKey(UniversityGroup, on_delete=CASCADE, blank=True, null=True)

    @property
    def score(self):
        return self.student_stages.all.aggregate(Sum('score'))['score__sum']


class Module(models.Model):
    '''Entity for representation of module work'''
    name = models.CharField('Module Name', max_length=100, null=False)
    description = models.TextField()
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now_add=True)
    tasks = models.ManyToManyField("main.Task", related_name='modules', through='main.TaskModule')

    @property
    def max_score(self):
        return sum(map(lambda x: x.max_score or 0, self.tasks.all()))


class Task(models.Model):
    '''A task in module work'''
    name = models.CharField('Task Name', max_length=100, null=False)
    description = models.TextField()
    pickle_dump = models.FileField(upload_to="tasks/")

    @property
    def max_score(self):
        return self.stages.all().aggregate(Sum('max_score'))['max_score__sum']


class Stage(models.Model):
    '''Represents a stage of the task'''
    name = models.CharField('Stage Name', max_length=100, null=False)
    max_score = models.IntegerField()
    description = models.TextField()
    task = models.ForeignKey("main.Task", on_delete=models.CASCADE, related_name='stages')
    students = models.ManyToManyField(Student, related_name='stages', through='main.StudentStage')


class StudentStage(models.Model):
    '''Binary relation student-stage for mark storing'''
    student = models.ForeignKey("main.Student", on_delete=models.CASCADE, related_name='student_stages')
    stage = models.ForeignKey("main.Stage", on_delete=models.CASCADE)
    score = models.IntegerField('Score for stage', null=False)


class TaskModule(models.Model):
    '''Binary relation task-module for re-using tasks in modules'''
    task = models.ForeignKey("main.Task", on_delete=models.CASCADE)
    module = models.ForeignKey("main.Module", on_delete=models.CASCADE)
