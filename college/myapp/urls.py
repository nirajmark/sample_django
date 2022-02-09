from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student/<int:student_id>', views.student_by_index, name='student_by_index')
]