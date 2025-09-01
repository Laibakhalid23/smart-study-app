from django.shortcuts import render,redirect
from .models import Subject,Deadline
from .forms import SubjectForm, DeadlineForm
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


