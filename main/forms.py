from django.forms import ModelForm, TextInput, Textarea, URLInput, Select

from main.models import Project, Experience


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "tech_stack",
            "code_url",
            "demo_url",
            "thumbnail",
        ]

        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "tech_stack": "Teknologi yang Digunakan",
            "code_url": "URL Kode (GitHub)",
            "demo_url": "URL Demo",
            "thumbnail": "URL Gambar Proyek",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Personal Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan proyekmu",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "placeholder": "Django, HTML, CSS",
                }
            ),
            "code_url": URLInput(
                attrs={
                    "placeholder": "https://github.com/username/repo",
                    "required": False,
                }
            ),
            "demo_url": URLInput(
                attrs={
                    "placeholder": "https://myproject.vercel.app",
                    "required": False,
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                    "required": False,
                }
            ),
        }

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
        ]

        labels = {
            "title": "Judul Pengalaman",
            "description": "Deskripsi",
            "category": "Kategori",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Staff Mentor PMB Fasilkom UI",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan pengalamanmu",
                    "rows": 3,
                }
            ),
            "category": Select(),
        }