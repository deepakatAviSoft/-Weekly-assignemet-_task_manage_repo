# urls.py
from django.urls import path
from .views import signup, user_login, home_page, todo_list, complete_task

urlpatterns = [
    path('', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('home/', home_page, name = 'home' ),
    path('todo/', todo_list, name='todo_list'),
    path('complete/<int:task_id>/', complete_task, name='complete_task'),
    # Other URL patterns
]


