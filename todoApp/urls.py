from django.urls import path
from . import views

# The url patterns are effectively "registering" the various parts
# of the Django application to respond to different URL requests.
urlpatterns = [
    path('', views.todo_list, name='list'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('update_todo/', views.update_todo, name='update_todo'),
]
