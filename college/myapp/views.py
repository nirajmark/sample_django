from re import S
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Student, Department
from .forms import StudentForm

def index(request):
  return HttpResponse('Hello World')

def student_by_index(request, student_id):
  student = Student.objects.get(pk=student_id)
  # return HttpResponse(f"name = {student.name} \n department name = {student.department.name}")
  return render(request, 'student.html', {'student': student})

def create_student(request):
  if request.method == 'POST':
    form = StudentForm(request.POST)
    if form.is_valid():
      student = Student(
        name=form.cleaned_data['name'],
        email=form.cleaned_data['email'],
        department=Department.objects.get(pk=form.cleaned_data['department']),
        gender=form.cleaned_data['gender'],
        subjects=', '.join(form.cleaned_data['subjects'])
      )
      student.save()
      return HttpResponseRedirect('/student/'+str(student.id))
  else:
    form = StudentForm()
  return render(request, 'create_student.html', {'form': form})
  
