from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('add',addTodo, name='add'),
    path('complete/<todo_id>', completeTodo,name='complete'),
    path('deletecomplete',deleteCompleted, name='deletecomplete'),
    path('deleteall',deleteAll,name='deleteall'),
]