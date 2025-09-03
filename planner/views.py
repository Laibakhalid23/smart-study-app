from django.shortcuts import render,redirect
from .models import Subject,Deadline, StudySession
from .forms import SubjectForm, DeadlineForm, StudySessionForm
def subject_list(request):
    user=request.user
    subjects=Subject.objects.filter(user=user) if user.is_authenticated else []
    if request.method=="POST":
        form=SubjectForm(request.POST)
        if form.is_valid():
            new_subject=form.save(commit=False)
            if user.is_authenticated:
                new_subject.user=user
                new_subject.save()
            return redirect("subject_list")
    else:
        form=SubjectForm()
    return render(request, "subjects.html", {"form": form, "subjects": subjects})

def deadline_list(request):
    deadlines = Deadline.objects.filter(subject__user=request.user)
    return render(request, "deadline_list.html", {"deadlines": deadlines})

def add_deadline(request):
    if request.method=="POST":
        form=DeadlineForm(request.POST)
        if form.is_valid():
            deadline=form.save(commit=False)
            if deadline.subject.user == request.user:
                deadline.save()
                return redirect("deadline_list")
    else:
        form = DeadlineForm()
    return render(request, "add_deadline.html", {"form": form})

def study_session_list(request):
    sessions=StudySession.objects.all()
    return render(request,"study_session_list.html",{"sessions":sessions})

def study_session_create(request):
    if request.method == "POST":
        form = StudySessionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("study_session_list")
    else:
        form = StudySessionForm()
    return render(request, "study_session_form.html", {"form": form})