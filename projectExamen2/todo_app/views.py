from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm

def create_todo(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_id_titles')
    return render(request, 'todo_app/todo_form.html', {'form': form})

def update_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('list_id_titles')
    return render(request, 'todo_app/todo_form.html', {'form': form})

def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect('list_id_titles')

def list_ids(request):
    todos = Todo.objects.all().values_list('id', flat=True)
    return render(request, 'todo_app/list_ids.html', {'todos': todos})

def list_id_titles(request):
    todos = Todo.objects.all()
    return render(request, 'todo_app/list_id_titles.html', {'todos': todos})

def list_unresolved(request):
    todos = Todo.objects.filter(resolved=False)
    return render(request, 'todo_app/list_unresolved.html', {'todos': todos})

def list_resolved(request):
    todos = Todo.objects.filter(resolved=True)
    return render(request, 'todo_app/list_resolved.html', {'todos': todos})

def list_id_user(request):
    todos = Todo.objects.all()
    return render(request, 'todo_app/list_id_user.html', {'todos': todos})

def list_resolved_user(request):
    todos = Todo.objects.filter(resolved=True)
    return render(request, 'todo_app/list_resolved_user.html', {'todos': todos})

def list_unresolved_user(request):
    todos = Todo.objects.filter(resolved=False)
    return render(request, 'todo_app/list_unresolved_user.html', {'todos': todos})
