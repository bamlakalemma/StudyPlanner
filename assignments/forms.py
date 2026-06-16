from django import forms
from .models import Assignment
from datetime import date 

class AssignmentForm(forms.ModelForm):

    class Meta:
        model = Assignment
        fields = ['title', 'description', 'due_date', 'course', 'completed']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'title': forms.TextInput(attrs={'placeholder': 'Enter assignment title'}),
        }
    def clean_due_date(self):
        due_date = self.cleaned_data['due_date']
        if due_date < date.today():
            raise forms.ValidationError("Due date cannot be in the past.")
        return due_date
    
class AssignmentFilterForm(forms.Form):
    completed = forms.BooleanField(required=False)