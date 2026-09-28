import os
import datetime
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied


from main.forms import ProjectForm, ExperienceForm
from main.models import Experience, Project

def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
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
        "last_login": last_login,
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
        "is_editor": is_editor(request.user),
    }
    return render(request, "experience.html", context)

def get_experience_json(request):
    experiences = Experience.objects.all()
    experience_json = serializers.serialize("json", experiences)
    return HttpResponse(experience_json, content_type="application/json")

@login_required(login_url="/login/")
def create_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied

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


@login_required(login_url="/login/")
def update_experience(request, experience_id):
    if not (request.user.is_superuser or is_editor(request.user)):
        raise PermissionDenied

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


@login_required(login_url="/login/")
def delete_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied

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

    projects_json = serializers.serialize(
        "json", projects, use_natural_foreign_keys=True
    )
    return HttpResponse(projects_json, content_type="application/json")

def show_projects(request):
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()

    is_editor = (
        request.user.is_authenticated
        and request.user.groups.filter(name="Editor").exists()
    )

    context = {
        "name": "Naurah Claradinda",
        "project_list": projects,
        "title_query": title_query,
        "is_editor": is_editor,
    }
    return render(request, "projects.html", context)

@login_required(login_url="/login/")
def create_project(request):
    if not request.user.is_superuser:
        raise PermissionDenied

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


@login_required(login_url="/login/")
def update_project(request, project_id):
    # Superuser dan Editor sama-sama boleh mengubah data
    is_editor = request.user.groups.filter(name="Editor").exists()
    if not (request.user.is_superuser or is_editor):
        raise PermissionDenied

    project = get_object_or_404(Project, pk=project_id)
    form = ProjectForm(request.POST or None, instance=project)
    password_error = None

    if request.method == "POST":
        if request.POST.get("edit_password") != os.getenv("EDIT_PASSWORD"):
            password_error = "Password salah!"
        elif form.is_valid():
            form.save()
            messages.success(request, "Proyek berhasil diperbarui!")
            return redirect("main:show_projects")

    context = {
        "name": "Naurah Claradinda",
        "form": form,
        "password_error": password_error,
        "project": project,
    }
    return render(request, "projects_form.html", context)


@login_required(login_url="/login/")
def delete_project(request, project_id):
    # Hanya superuser (pemilik portofolio) yang boleh menghapus
    if not request.user.is_superuser:
        raise PermissionDenied

    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        if request.POST.get("edit_password") != os.getenv("EDIT_PASSWORD"):
            messages.error(request, "Password salah!")
            return redirect("main:show_projects")

        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

@login_required(login_url="/login/")
def toggle_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_projects")

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Naurah Claradinda",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Naurah Claradinda",  # ganti sesuai nama kamu
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response



def is_editor(user):
    return user.is_authenticated and user.groups.filter(name="Editor").exists()