from django.db import models

# Create your models here.

class Parent(models.Model):
  name = models.CharField(max_length=100, default='ABDULLAHI USMAN')
  occupation = models.CharField(max_length=100, default='Backend Engineer')
  
  def __str__(self):
    return f"{self.name}"

############# 1 to 1 #############


class Student(models.Model):
  parent=models.ForeignKey(Parent, on_delete=models.SET_NULL, null=True)
  name = models.CharField(max_length=100)
  age = models.IntegerField(blank=True, null= True)
  address=models.CharField(max_length=255)
  gender=models.CharField(max_length=25)
  nationality=models.CharField(max_length=100, default="Nigerian")
  parent_number=models.BigIntegerField()
  hobby=models.CharField(max_length=255, null= True)

  def __str__(self):
    return f"{self.name}"



