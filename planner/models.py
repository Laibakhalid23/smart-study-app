from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Subject(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    DIFFICULTY_CHOICES = [(i, str(i)) for i in range(1, 6)]
    difficulty=models.PositiveSmallIntegerField(choices=DIFFICULTY_CHOICES, default=3)

    def __str__(self):
        return self.name
    
class Deadline(models.Model):
        subject=models.ForeignKey(Subject,on_delete=models.CASCADE,related_name="deadlines")
        due_date=models.DateField()

        def __str__(self):
             return f"{self.subject.name} due {self.due_date}"
        
class StudySession(models.Model):
        subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
        duration=models.PositiveIntegerField(help_text="minutes")
        date=models.DateField(default=timezone.now)

        def __str__(self):
              return f"{self.subject.name} {self.duration} min on {self.date}"





