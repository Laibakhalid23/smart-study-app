from django import forms
from .models import Subject,Deadline, StudySession

class SubjectForm(forms.ModelForm):
    class Meta:
        model=Subject
        fields=["name","difficulty"]

class DeadlineForm(forms.ModelForm):
    class Meta:
        model=Deadline
        fields=["subject","due_date"]
        widgets={"due_date":forms.DateInput(attrs={'type':'date'})}

class StudySessionForm(forms.ModelForm):
    class Meta:
        model = StudySession
        fields = ["subject", "duration", "date"]
