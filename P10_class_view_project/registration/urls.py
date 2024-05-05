from django.urls import path
from . import views
from .views import StudentDetailView, StudentListView

urlpatterns = [
    path('courses/', views.course_list, name = 'course_list'),
    path('courses/<int:course_id>/students/', views.student_list, name = 'student_list'),
    path('add_course/', views.add_course, name = 'add_course'),
    path('add_student/', views.add_student, name = 'add_student'),
    path('assign_students/<int:course_id>/', views.assign_students, name = 'assign_students'),
    path('students/', StudentListView.as_view(), name = 'student_list'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name = 'student_detail'),
]
