"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from planner.views import subject_list,deadline_list,add_deadline,study_session_list, study_session_create


def home(request):
    return render(request, "home.html")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("subjects/", subject_list, name="subject_list"),
    path("deadlines/", deadline_list, name="deadline_list"),
    path("deadlines/add/", add_deadline, name="add_deadline"),
    path("sessions/", study_session_list, name="study_session_list"),
    path("sessions/add/", study_session_create, name="study_session_create"),
]

