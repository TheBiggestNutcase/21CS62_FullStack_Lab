from django.urls import path
from . import views

urlpatterns = [
    path('project-form/', views.project_form, name = 'project_form'),
    path('success/', views.success, name='success'),
]