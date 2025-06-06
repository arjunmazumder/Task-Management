from django.db import models

# Project table
class Project(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name
    


# Employee table
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name



# task table
class Task(models.Model):
    STATUS_CHOICES=[
        ('PENDING','Pending'),
        ('IN_PROGRESS','In Progress'),
        ('COMPLETED','Completed')
    ]
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=1) #Relation
    assignedTo = models.ManyToManyField(Employee) #Relation
    title = models.CharField(max_length=250)
    description = models.TextField()
    due_date = models.DateField()
    status=models.CharField(max_length=15,choices=STATUS_CHOICES,default='PENDING')
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



# task detail table
class TaskDetail(models.Model):
    HIGH='H'
    MEDIUM='M'
    LOW='L'
    PRIORITY_OPTIONS = (
        ( HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low')

    )
    task = models.OneToOneField(
        Task, on_delete=models.CASCADE,
        related_name='details'
        ) #one to one relation between task and task detail
    # assignedTo = models.CharField(max_length=150)
    priority = models.CharField(max_length=1, choices=PRIORITY_OPTIONS, default=LOW) 
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Details for Task {self.task.title}"



