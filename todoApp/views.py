from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from .models import Todo


def add_todo(request):
    if request.method == "POST":
        title = request.POST.get('todo_title')
        if title:
            Todo.objects.create(title=title, status=False)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'list.html', {'todos': todos})


def update_todo(request):
    if request.method == 'POST':
        todo = get_object_or_404(Todo, id=request.POST.get('todo_id'))
        todo.status = not todo.status
        todo.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
