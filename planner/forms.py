from django import forms
from .models import Subject 
from .models import Deadline

class SubjectForm(forms.ModelForm):
    class Meta:
        model=Subject
        fields=["name","difficulty"]

class DeadlineForm(forms.ModelForm):
    class Meta:
        model=Deadline
        fields=["subject","due_date"]
        widgets={"due_date":forms.DateInput(attrs={'type':'date'})}
