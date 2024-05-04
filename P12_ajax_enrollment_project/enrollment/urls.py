from django.urls import path
from . import views

urlpatterns = [
    path('', views.registration_page, name='registration_page'),
    path('register/', views.register_student, name='register_student'),
]