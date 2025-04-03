from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Project

class ProjectModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="testuser", password="password123")
        self.project = Project.objects.create(
            name="Test Project",
            description="This is a test project.",
            start_date="2025-01-01",
            end_date="2025-12-31",
            owner=self.user
        )

    def test_project_creation(self):
        self.assertEqual(self.project.name, "Test Project")
        self.assertEqual(self.project.owner.username, "testuser")
