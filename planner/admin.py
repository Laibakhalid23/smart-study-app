from django.contrib import admin
from .models import Subject,Deadline,StudySession

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display=("name","user","difficulty")
    list_filter=("difficulty","user")
    search_fields=("name","user__username")

@admin.register(Deadline)
class DeadlineAdmin(admin.ModelAdmin):
    list_display=("subject","due_date")
    list_filter=("due_date","subject")
    search_fields=("subject__name",)

@admin.register(StudySession)
class StudySessionAdmin(admin.ModelAdmin):
    list_display=("subject","duration","date")
    list_filter=("date","subject")
    search_fields=("subject__name",)


