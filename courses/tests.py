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

    def test_course_create_view(self):
        response=self.client.post(reverse("course_create"),
                                  {
            "owner":self.user.id,
            "subject":"another subject",
            "title":"chapter two",
            "slug":"chapter-two",
            "overview":"description",

        },)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Course.objects.last().subject, "another subject")
        self.assertEqual(Course.objects.last().title, "chapter two")
        self.assertEqual(Course.objects.last().slug, "chpater-two")
        self.assertEqual(Course.objects.last().overview,"description")

    def test_course_update_view(self):
        response=self.client.post(reverse("course_edit", args="1"),{
            "title":"updated title",
            "overview":"updated description",
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Course.objects.last().title, "updated title")
        self.assertEqual(Course.objects.last().overview, "updated description")
        