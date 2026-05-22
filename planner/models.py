from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings 
import assignments.models



# Create your models here.
class StudyTask(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    planned_date = models.DateField()
    duration = models.IntegerField(help_text="Duration in minutes")
    related_assignment = models.ForeignKey(assignments.models.Assignment, on_delete=models.CASCADE) 
    completed = models.BooleanField(default=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title