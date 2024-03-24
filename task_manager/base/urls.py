# urls.py
from django.urls import path
from .views import signup, user_login, home_page

urlpatterns = [
    path('', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('home/', home_page, name = 'home' )
    # Other URL patterns
]


