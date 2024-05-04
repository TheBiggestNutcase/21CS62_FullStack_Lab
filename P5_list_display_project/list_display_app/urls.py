from django.urls import path
from . import views

urlpatterns = [
    path('fruits/', views.fruit_list, name='fruit_list'),  # This is for fruits
    path('students/', views.student_list, name='student_list'),  # This is for students
]
