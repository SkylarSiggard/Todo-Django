from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='list'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('update_todo/', views.update_todo, name='update_todo'),
]
