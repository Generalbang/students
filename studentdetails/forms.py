from django import forms
from .models import *

class Parent_Form(forms.ModelForm):
  name = forms.CharField(label='name', required=True)
  occupation = forms.CharField(label='occupation')

  class Meta:
    model = Parent
    fields = ['name','occupation']


class Student_Form(forms.ModelForm):
  name = forms.CharField(label='Name', required=True)
  gender = forms.CharField(label='Gender', required=True)
  nationality = forms.CharField(label='Nationality', required=True)
  age = forms.IntegerField(label='Age', required=True)
  parent_number = forms.IntegerField(label='Parent Phone Number', required=True)
  address = forms.CharField(label='Address', required=True)
  hobby = forms.CharField(label='Hobby')

  class Meta:
    model = Student
    fields = ['parent','name','gender','nationality','age','parent_number','address','hobby',]