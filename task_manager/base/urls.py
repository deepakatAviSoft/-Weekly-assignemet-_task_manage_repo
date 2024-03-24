# urls.py
from django.urls import path
from .views import signup

urlpatterns = [
    path('', signup, name='signup'),
    # Other URL patterns
]