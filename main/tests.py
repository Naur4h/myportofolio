import os

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.forms import ProjectForm, ExperienceForm
from main.models import Experience, Project


class MainTest(TestCase):
    def setUp(self):
        os.environ["EDIT_PASSWORD"] = "test-password"
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="part-time",
        )
        self.project = Project.objects.create(
            title="Personal Portfolio Website",
            description="Website portofolio pribadi dibuat dengan Django.",
            tech_stack="Django, HTML, CSS",
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Part-Time")
        self.assertContains(response, "Sedang berlangsung")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "Belum ada pengalaman yang ditambahkan.")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "Selesai")
        self.assertNotContains(response, "Sedang berlangsung")

    def test_create_project_page_is_accessible(self):
        response = self.client.get(reverse("main:create_project"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "projects_form.html")

    def test_create_project_via_post(self):
        response = self.client.post(reverse("main:create_project"), {
            "title": "New Test Project",
            "description": "A project created via form submission.",
            "tech_stack": "Python, Django",
            "edit_password": "test-password",
        })

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Project.objects.filter(title="New Test Project").exists())

    def test_delete_project(self):
        response = self.client.post(
            reverse("main:delete_project", args=[self.project.id]),
            {"edit_password": "test-password"},
        )

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Project.objects.filter(id=self.project.id).exists())

    def test_get_projects_json(self):
        response = self.client.get(reverse("main:get_projects_json"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/json")

    def test_get_projects_json_with_search(self):
        response = self.client.get(
            reverse("main:get_projects_json"), {"title": "Personal"}
        )

        self.assertContains(response, "Personal Portfolio Website")

    def test_projects_page_search_shows_no_results_message(self):
        response = self.client.get(
            reverse("main:show_projects"), {"title": "NonexistentProject"}
        )

        self.assertContains(response, "Tidak ada proyek dengan nama tersebut.")

    def test_create_experience_page_is_accessible(self):
        response = self.client.get(reverse("main:create_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience_form.html")

    def test_create_experience_via_post(self):
        response = self.client.post(reverse("main:create_experience"), {
            "title": "New Experience",
            "description": "Created via form submission.",
            "category": "volunteer",
            "edit_password": "test-password",
        })

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Experience.objects.filter(title="New Experience").exists())

    def test_update_experience_page_is_accessible(self):
        response = self.client.get(
            reverse("main:update_experience", args=[self.experience.id])
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience_form.html")

    def test_update_experience_via_post(self):
        response = self.client.post(
            reverse("main:update_experience", args=[self.experience.id]),
            {
                "title": "Updated Title",
                "description": self.experience.description,
                "category": self.experience.category,
                "edit_password": "test-password",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.experience.refresh_from_db()
        self.assertEqual(self.experience.title, "Updated Title")

    def test_delete_experience(self):
        response = self.client.post(
            reverse("main:delete_experience", args=[self.experience.id]),
            {"edit_password": "test-password"},
        )

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Experience.objects.filter(id=self.experience.id).exists())

    def test_get_experience_json(self):
        response = self.client.get(reverse("main:get_experience_json"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/json")
        self.assertContains(response, "Asisten Dosen PBP")