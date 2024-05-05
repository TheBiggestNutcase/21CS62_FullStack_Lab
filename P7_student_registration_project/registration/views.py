from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Course
from .forms import CourseForm, StudentForm, CourseAssignForm

# Create your views here.

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses':courses})

def student_list(request, course_id):
    course = get_object_or_404(Course, id = course_id)
    students = course.students.all()
    return render(request, 'student_list.html', {'students':students})

def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'add_course.html', {'form':form})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form':form})

def assign_students(request, course_id):
    course = get_object_or_404(Course, id = course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance = course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance = course)
    return render(request, 'assign_students.html', {'form':form, 'course':course})

def assign_students(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = CourseAssignForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseAssignForm(instance=course)
    return render(request, 'assign_students.html', {'form': form, 'course': course})