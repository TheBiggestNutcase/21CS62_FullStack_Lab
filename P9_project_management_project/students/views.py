from django.shortcuts import render, redirect
from .forms import ProjectForm

# Create your views here.

def project_form(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ProjectForm()
    return render(request, 'students/project_form.html', {'form':form})

def success(request):
    return render(request, 'students/success.html')
