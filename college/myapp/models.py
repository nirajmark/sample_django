from django.db import models

class Department(models.Model):
  name = models.CharField(max_length=200)
  department_hod = models.CharField(max_length=200)

class Student(models.Model):
  name = models.CharField(max_length=200)
  email = models.CharField(max_length=200)
  department = models.ForeignKey(Department, on_delete = models.CASCADE)