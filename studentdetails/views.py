from django.shortcuts import render, redirect
from django.template import loader
from . import models
from .models import *
from .forms import *
from datetime import datetime, date
from django.http import HttpResponse

# Create your views here.

def home(request):
  html = loader.get_template('home.html')
  today = date.today()
  # save_person = Person(name='OJO DARE', age=35, address='Aso Rock', phone='6363636363636', nationality='Nigerian' )
  #  save_person.save()

  person = Student.objects.all()

  con={
    person
  }
  return HttpResponse(html.render(con, request))

def register(request):
  html = loader.get_template('student_reg.html')
  if request.method == 'POST':
    form = Student_Form(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/studentdetails/students')
    else:
      return render(request, 'student_reg.html', {'form' : form})
  form = Student_Form()
  con = {
    'form' : form
  }
  return HttpResponse(html.render(con, request))

def students(request):
  html = loader.get_template('students.html')
  student = Student.objects.all()
  print(Student.parent)

  con={
    'student' : student
  }
  return HttpResponse(html.render(con, request))

def add(request):
  html = loader.get_template('student_reg.html')
  form = Student_Form()
  return redirect('student_reg')

def delete(request, id):
  Student.objects.get(id = id).delete()
  return redirect('/studentdetails/students')

# """ def edit(request, id):
#   student = Student.objects.get(id = id) """
