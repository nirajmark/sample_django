from re import S
from django.shortcuts import render
from django.http import HttpResponse

from .models import Student, Department

def index(request):
  return HttpResponse('Hello World')

def student_by_index(request, student_id):
  student = Student.objects.get(pk=student_id)
  # return HttpResponse(f"name = {student.name} \n department name = {student.department.name}")
  return render(request, 'student.html', {'student': student})
  
