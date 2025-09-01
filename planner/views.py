from django.shortcuts import render,redirect
from .models import Subject
from .forms import SubjectForm
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

