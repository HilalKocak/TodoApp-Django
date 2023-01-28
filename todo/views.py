from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Todo
# Create your views here.


def home_view(request):
    # todos = Todo.objects.all()
    # todos = Todo.objects.filter(is_active=True)
    # todos = Todo.objects.filter(title__icontains="todo")
    todos = Todo.objects.filter(
        is_active = True,
        #title__icontains="Todo",
    )
    context = dict(
        todos = todos,
    )
    return render(request, 'todo/todo_list.html', context)

# def todo_detail_view(request, id):
#     try:
#         todo=Todo.objects.get(pk=id)
#         context=dict(
#             todo=todo,
#         )
#         return render(request, 'todo/todo_detail.html', context)
#     except Todo.DoesNotExist:
#         raise Http404

def todo_detail_view(request, id):
    
    todo=get_object_or_404(Todo,pk=id)
    context=dict(
        todo=todo,
    )
    return render(request, 'todo/todo_detail.html', context)
