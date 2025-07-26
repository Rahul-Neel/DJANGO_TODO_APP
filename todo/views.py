from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from todo.models import Task

# Create your views here.

def addtask(request):
    if request.method == 'POST':
        task_text = request.POST.get('task', '').strip()

        if not task_text:
            # Render home page with error
            # Assuming you're listing tasks on the home page
            task = Task.objects.filter(is_completed=False)
            completed_task = Task.objects.filter(is_completed=True)
            return render(request, 'home.html', {
                'error': "Please enter a task",
                'tasks': task,
                'c_tasks' : completed_task,

            })

        Task.objects.create(task=task_text)
        return redirect('home')
    else:
        return redirect('home')


def mark_as_done(request, pk):
    data = get_object_or_404(Task, pk=pk)
    data.is_completed = True
    data.save()
    return redirect('home')

def mark_as_undone(request, pk):
    data = get_object_or_404(Task, pk=pk)
    data.is_completed = False
    data.save()
    return redirect('home')

def delete(request, pk):
    data = get_object_or_404(Task, pk=pk)
    data.delete()
    return redirect('home')

def edit_task(request, pk):
    get_task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        edit_data = request.POST['task']
        get_task.task = edit_data
        get_task.save()
        return redirect('home')
    
    else:
        context={
            'data':get_task
        }
        return render(request, 'edit.html' , context)







