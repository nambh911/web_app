from django.shortcuts import render, get_object_or_404, redirect
from .models import TodoItem
from .forms import TodoForm

def index(request):
    todos = TodoItem.objects.all()
    return render(request, 'todoapp/index.html', {'todos': todos})

def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoForm()
    return render(request, 'todoapp/add_todo.html', {'form': form})

def update_todo(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todoapp/update_todo.html', {'form': form})

def delete_todo(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('index')
    return render(request, 'todoapp/delete_todo.html', {'todo': todo})
