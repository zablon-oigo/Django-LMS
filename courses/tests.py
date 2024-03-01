from django.test import TestCase
from .models import Course
from django.urls import reverse
from django.contrib.auth import get_user_model

class CourseTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user=get_user_model().objects.create_user(
            username="testuser",
            password="secret",
            email="testuser@mail.com"
        )
        cls.course=Course.objects.create(
            owner=cls.user,
            subject="New subject",
            title="chapter one",
            slug="chapter-one",
            overview="description",
        )

    def test_model_content(self):
        self.assertEqual(self.course.owner.username, "testuser")
        self.assertEqual(self.course.subject, "New subject")
        self.assertEqual(self.course.slug, "chapter-one")
        self.assertEqual(self.course.overview, "description")

