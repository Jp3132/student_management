# students/views.py
from django.shortcuts import render
from .models import Student
from .forms import StudentForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator

def student_list(request):
    query = request.GET.get('q')
    if query:
        students_list = Student.objects.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query)
        )
    else:
        students_list = Student.objects.all()

    paginator = Paginator(students_list, 10)  # Show 10 students per page
    page_number = request.GET.get('page')
    students = paginator.get_page(page_number)

    context = {'students': students}
    return render(request, 'students/student_list.html', context)

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    context = {'student': student}
    return render(request, 'students/student_detail.html', context)

@login_required
def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    context = {
        'form': form,
        'form_title': 'Add New Student',
    }
    return render(request, 'students/student_form.html', context)
    pass

@login_required
def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_detail', pk=pk)
    else:
        form = StudentForm(instance=student)
    context = {
        'form': form,
        'form_title': 'Edit Student Information',
    }
    return render(request, 'students/student_form.html', context)
    
    

