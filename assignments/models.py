from django.db import models
from django.contrib.auth.models import User
import courses.models 

# Create your models here.
class Assignment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    course = models.ForeignKey(courses.models.Course, on_delete=models.CASCADE) 
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title