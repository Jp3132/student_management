# students/views.py
from django.shortcuts import render
from .models import Student

def student_list(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'students/student_list.html', context)

from django.shortcuts import get_object_or_404

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    context = {'student': student}
    return render(request, 'students/student_detail.html', context)

def student_add(request):
    # Placeholder for form handling
    pass

def student_edit(request, pk):
    # Placeholder for form handling
    pass

