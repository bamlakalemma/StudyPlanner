from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=200)
    course_code = models.CharField(max_length=10)
    instructor = models.CharField(max_length=100)
    semester = models.CharField(max_length=20)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title