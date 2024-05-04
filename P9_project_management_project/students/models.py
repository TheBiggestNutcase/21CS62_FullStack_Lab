from django.db import models

# Create your models here.

class Project(models.Model):
    student_name = models.CharField(max_length=100)
    topic = models.CharField(max_length=200)
    languages_used = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)

    def __str__(self):
        return self.student_name
