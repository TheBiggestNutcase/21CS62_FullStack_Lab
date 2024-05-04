from django.shortcuts import render
from django.http import JsonResponse
from .forms import StudentForm
from .models import Course

# Create your views here.

def registration_page(request):
    courses = Course.objects.all()
    return render(request, 'enrollment/registration_page.html', {'courses': courses})

def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            return JsonResponse({'success':True, 'student_id':student.id})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success':False, 'errors':errors}, status=400)
    else:
        return JsonResponse({'success':False, 'message':'Invalid request method'}, status = 400)
