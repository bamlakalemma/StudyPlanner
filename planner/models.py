from django.db import models
from django.contrib.auth.models import User
import assignments.models


# Create your models here.
class StudyTask(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    planned_date = models.DateField()
    duration = models.IntegerField(help_text="Duration in minutes")
    related_assignment = models.ForeignKey(assignments.models.Assignment, on_delete=models.CASCADE) 
    completed = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title