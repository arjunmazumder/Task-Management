from django.shortcuts import render,redirect
from django.http import HttpResponse
from tasks.forms import TaskForm,TaskModelForm, TaskDetailModelForm
from tasks.models import Employee,Task
from django.db.models import Q, Count
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, login_required, permission_required

def is_manager(user):
    return user.groups.filter(name='Manager').exists()

def is_employee(user):
    return user.groups.filter(name='Employee').exists()
# Create your views here.
@user_passes_test(is_manager, login_url='no-permission')
def manager_dashboard(request):

    type = request.GET.get('type','all')

    counts = Task.objects.aggregate(
        total_task=Count('id'),
        completed_task=Count('id', filter=Q(status="COMPLETED")),
        task_in_progress=Count('id', filter=Q(status="IN_PROGRESS")),
        pending_task=Count('id', filter=Q(status="PENDING")),
    )

    #Retriving data

    Base_query = Task.objects.select_related('details').prefetch_related('assignedTo')
    if type == 'completed_task':
        tasks = Base_query.filter(status='COMPLETED')
    elif type == 'task_in_progress':
        tasks = Base_query.filter(status='IN_PROGRESS')   
    elif type == 'pending_task':
        tasks = Base_query.filter(status='PENDING') 
    elif type == 'all':
        tasks = Base_query.all()

    context = {
        "tasks" : tasks,
        "counts" : counts
    }

    return render(request,"dashboard/managerdashboard.html", context)


@user_passes_test(is_employee, login_url='no-permission')
def employee_dashboard(request):
    return render(request,"dashboard/userdashboard.html")

@login_required
@permission_required("tasks.add_Tasks", login_url='no-permission')
def create_task(request):
    task_form = TaskModelForm()
    task_detail_form = TaskDetailModelForm()
    if request.method == "POST":
        task_form = TaskModelForm(request.POST)
        task_detail_form = TaskDetailModelForm(request.POST)
        if task_form.is_valid() and task_detail_form.is_valid():
            task = task_form.save()
            task_detail = task_detail_form.save(commit=False)
            task_detail.task = task
            task_detail.save()  
            messages.success(request, "Task Created Successfuly!!")
            return redirect('creat-task')

    context = {"task_form": task_form, "task_detail_form" : task_detail_form}
    return render(request,"task_form.html", context)


@login_required
@permission_required("tasks.change_Tasks", login_url='no-permission')
def update_task(request, id):
    task = Task.objects.get(id=id)
    task_form = TaskModelForm(instance=task)
    if task.details:
        task_detail_form = TaskDetailModelForm(instance=task.details)
    if request.method == "POST":
        task_form = TaskModelForm(request.POST, instance=task)
        task_detail_form = TaskDetailModelForm(request.POST, instance=task.details)
        if task_form.is_valid() and task_detail_form.is_valid():
            task_form = task_form.save()
            task_detail = task_detail_form.save(commit=False)
            task_detail.task = task
            task_detail_form.save()  
            messages.success(request, "Task updated Successfuly!!")
            return redirect('update-task',id)

    context = {"task_form": task_form, "task_detail_form" : task_detail_form}
    return render(request,"task_form.html", context)



@login_required
@permission_required("tasks.delete_Tasks", login_url='no-permission')
def delete_task(request, id):
    if request.method == 'POST':
        task = Task.objects.get(id=id)
        task.delete()
        messages.success(request, 'Task deleted Successfully!!!')
        return redirect('manager_dashboard')
    else:
        messages.error(request, 'Something went wrong!!')   
        return redirect('manager_dashboard')



@login_required
@permission_required("tasks.view_Tasks", login_url='no-permission')
def view_task(request):
    # Retrive all data from task models
    tasks = Task.objects.all()
    return render(request,'show_task.html',{'tasks':tasks})