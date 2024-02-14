from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Todo


# Views.py file contains the "business logic", like a request or queries file.
# Receives HTTP requests and returns HTTP responses.

def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'list.html', {'todos': todos})


def add_todo(request):  # See the form in base.html
    if request.method == "POST":
        title = request.POST.get('todo_title')
        if title:
            Todo.objects.create(title=title, status=False)
        else:
            return todo_list(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def update_todo(request):  # See the form in list.html
    if request.method == 'POST':
        todo = Todo.objects.get(id=request.POST.get('todo_id'))
        todo.status = not todo.status
        todo.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
