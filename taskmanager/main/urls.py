from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name = 'home'),
    path('about', about, name='about'),
    path('courses', courses, name='courses'),
    path('users', users, name = 'users'),
    path('login/', accounts, name = 'login')
]
