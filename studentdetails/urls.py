from django import views
from django.urls import path
from . import views
from .views import *

app_name = 'studentdetails'

urlpatterns = [
  path("home/", views.home, name='home'),
  path("register/", views.register, name='student_reg'),
  path("register/", views.add, name='student_reg'),
  path("students/", views.students, name='students'),
  path('del/<int:id>/', views.delete, name='delete'),
]


# """ path("register/", views.register, name='register'),
#  path('todo/', views.todo, name='todo'),
#  path('del/<int:id>/', views.delete, name='delete') """