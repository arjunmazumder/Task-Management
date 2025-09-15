from django.contrib import admin
from tasks.models import Project, Employee, Task, TaskDetail

# Register your models here.
admin.site.register(Project)
admin.site.register(Employee)
admin.site.register(Task)
admin.site.register(TaskDetail)
