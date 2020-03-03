from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test


from .models import Task
from .forms import TaskForm

@login_required
def taskList (request):
    search = request.GET.get('search')
    filter = request.GET.get('filter')
    if search:
        tasks = Task.objects.filter(title__icontains=search)#{DESATIVADO regra de negocio},user=request.user)
    
    elif filter:
        tasks = Task.objects.filter(done=filter, user=request.user)

    else:
        tasks_list = Task.objects.all().order_by('-created_at')#{DESATIVADO regra de negocio}.filter(user=request.user)
        paginator = Paginator(tasks_list, 3)
        page = request.GET.get('page')
        tasks = paginator.get_page(page)
        
    return render(request, 'task/list.html', {'tasks': tasks})

@login_required
def taskView(request, id):  
    task = get_object_or_404(Task, pk=id)
    return render(request, 'task/task.html', {'task':task})


@user_passes_test(lambda u: u.is_superuser) #apenas superusuario poderá adicionar
def newTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)        
        if form.is_valid():
                task = form.save(commit=False)
                task.done = 'doing'
                #{DESATIVADO regra de negocio}task.user = request.user
                task.save()
                return redirect('/logged/task')
    else:
        form = TaskForm()
        return render(request, 'task/addtask.html', {'form': form})

@login_required
def editTask(request, id):
    task = get_object_or_404(Task, pk =id)
    form = TaskForm(instance=task)
 
    if (request.method == 'POST'):
        form = TaskForm(request.POST, instance=task)
 
        if(form.is_valid()):
            task.save()
            return redirect('/logged/task')
        else:
            return render(request, 'task/edittask.html', {'form':form, 'task':task})
    else:
        return render(request, 'task/edittask.html', {'form':form, 'task':task})

@login_required
def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()

    messages.info(request, 'Tarefa deletada com sucesso!')

    return redirect('/logged/task')

@login_required
def changeStatus(request, id):
    task = get_object_or_404(Task, pk=id)
 
    if(task.done == 'doing'):
        task.done = 'done'
    else:
        task.done = 'doing'
    task.save()
    return redirect('/logged/task')

