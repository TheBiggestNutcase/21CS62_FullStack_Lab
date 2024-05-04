from django.shortcuts import render

# Create your views here.

def fruit_list(request):
    fruits = ['Apple', 'Banana', 'Orange', 'Grapes', 'Watermelon']
    return render(request, 'list_display_app/fruit_list.html', {'fruits':fruits})

def student_list(request):
    students = ['John', 'Emma', 'Alice', 'Michael', 'Sophia']
    return render(request, 'list_display_app/student_list.html', {'student':students})