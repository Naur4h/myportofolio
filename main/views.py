from django.shortcuts import render

from main.models import Experience


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
    context = {
        "name": "Naurah Claradinda",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)