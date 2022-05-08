from django.contrib import admin
from main.models import Stage, Student, StudentStage, Task, TaskModule, UniversityGroup, Module
# Register your models here.

admin.site.register(UniversityGroup)
admin.site.register(Student)
admin.site.register(Module)
admin.site.register(Task)
admin.site.register(Stage)
admin.site.register(StudentStage)
admin.site.register(TaskModule)
