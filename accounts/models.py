from django.db import models
from django.contrib.auth.models import User
# Create your models here.

YEAR_CHOICES = [
    (1, "Year 1"),
    (2, "Year 2"),
    (3, "Year 3"),
    (4, "Year 4"),
]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    field_of_study = models.CharField(max_length=100)
    year_of_study = models.IntegerField(choices=YEAR_CHOICES)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
