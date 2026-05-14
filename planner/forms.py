from django import forms
from .models import StudyTask

class StudyTaskForm(forms.ModelForm):

    class Meta:
        model = StudyTask
        fields = [
            'title',
            'description',
            'planned_date',
            'duration',
            'related_assignment',
            'completed'
        ]