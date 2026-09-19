import os

from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.forms import ProjectForm, ExperienceForm
from main.models import Experience, Project

def show_main(request):
    context = {
        "name": "Naurah Claradinda",
        "npm": "2506657163",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "I am currently studying Computer Science at the University of Indonesia. "
            "As a beginner in web development, I have a strong enthusiasm for learning "
            "how modern web technologies work and how they can be used to create useful "
            "and user-friendly solutions."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    json_response = get_experience_json(request)

    experiences = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    experiences = [exp.object for exp in experiences]

    context = {
        "name": "Naurah Claradinda",
        "experience_list": experiences,
    }
    return render(request, "experience.html", context)

def get_experience_json(request):
    experiences = Experience.objects.all()
    experience_json = serializers.serialize("json", experiences)
    return HttpResponse(experience_json, content_type="application/json")


def create_experience(request):
    form = ExperienceForm(request.POST or None)
    password_error = None

    if request.method == "POST":
        if request.POST.get("edit_password") != os.getenv("EDIT_PASSWORD"):
            password_error = "Password salah!"
        elif form.is_valid():
            form.save()
            messages.success(request, "Pengalaman baru berhasil ditambahkan!")
            return redirect("main:show_experience")

    context = {
        "name": "Naurah Claradinda",
        "form": form,
        "password_error": password_error,
    }
    return render(request, "experience_form.html", context)


def update_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)
    form = ExperienceForm(request.POST or None, instance=experience)
    password_error = None

    if request.method == "POST":
        if request.POST.get("edit_password") != os.getenv("EDIT_PASSWORD"):
            password_error = "Password salah!"
        elif form.is_valid():
            form.save()
            messages.success(request, "Pengalaman berhasil diperbarui!")
            return redirect("main:show_experience")

    context = {
        "name": "Naurah Claradinda",
        "form": form,
        "password_error": password_error,
        "experience": experience,
    }
    return render(request, "experience_form.html", context)


def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        if request.POST.get("edit_password") != os.getenv("EDIT_PASSWORD"):
            messages.error(request, "Password salah!")
            return redirect("main:show_experience")

        experience.delete()
        messages.success(request, "Pengalaman berhasil dihapus!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")

def show_projects(request):
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Naurah Claradinda",
        "project_list": projects,
        "title_query": title_query,
    }
    return render(request, "projects.html", context)
def create_project(request):
    form = ProjectForm(request.POST or None)
    password_error = None

    if request.method == "POST":
        if request.POST.get("edit_password") != os.getenv("EDIT_PASSWORD"):
            password_error = "Password salah!"
        elif form.is_valid():
            form.save()
            messages.success(request, "Proyek baru berhasil ditambahkan!")
            return redirect("main:show_projects")

    context = {
        "name": "Naurah Claradinda",
        "form": form,
        "password_error": password_error,
    }
    return render(request, "projects_form.html", context)

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        if request.POST.get("edit_password") != os.getenv("EDIT_PASSWORD"):
            messages.error(request, "Password salah!")
            return redirect("main:show_projects")

        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")