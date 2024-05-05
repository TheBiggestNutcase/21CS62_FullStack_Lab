from django import forms
from .models import Student, Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description', 'students']
        widgets = {
            'students': forms.CheckboxSelectMultiple,
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email']

class CourseAssignForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['students']
        widgets = {
            'students': forms.CheckboxSelectMultiple,
        }
