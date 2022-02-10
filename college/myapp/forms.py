from cProfile import label
from django import forms
from .models import Department

class StudentForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.CharField(label='Email', max_length=100)
    departments = list(
      map(lambda department: (department.id, department.name), Department.objects.all()));
    department = forms.ChoiceField(label='Department', choices=departments)

    subjects = (
      ("Science", "Science"),
      ("Math", "Math"),
      ("English", "English"),
      ("Computer", "Computer"),
    )
    subjects = forms.MultipleChoiceField(
      label='Subjects', widget=forms.CheckboxSelectMultiple, choices=subjects)

    genders = (
      ("Male", "Male"),
      ("Female", "Female"),
      ("Other", "Other"),
    )
    gender = forms.ChoiceField(
      label='Gender', widget=forms.RadioSelect, choices=genders)
    