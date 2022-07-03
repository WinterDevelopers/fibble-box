import datetime
from time import timezone

from django.test import TestCase

from .models import Writer, Post, Comment


# Create your tests here.
class BaseSetUp(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.writer = Writer.objects.create(
            first_name="Kelvin",
            last_name="Testing",
            bio="I'm a fan of Test driven development",
            date_joined=datetime.datetime(2022, 6, 3)
        )

        cls.post = Post.objects.create(
            title="Test case",
            # slug=""
            text="I'm testing the post model",
            writer=cls.writer,
        )

        cls.comment = Comment.objects.create(
            username="Christian",
            comment="was the test passing?"
        )


class WriterModelTest(BaseSetUp):
    def test_str_method(self):
        writer = self.writer
        self.assertEqual(Writer.__str__(writer), "Kelvin")

    def test_get_absolute_url_method(self):
        writer = self.writer
        self.assertEqual(Writer.get_absolute_url(writer), "Kelvin Testing")


class PostModelTest(BaseSetUp):
    def test_str_method(self):
        post = self.post
        self.assertEqual(Post.__str__(post), "Test case")

    def test_save_method_adds_a_slug_when_not_provided(self):
        post = self.post
        self.assertEqual(post.slug, "test-case")

    def test_get_absolute_url_method(self):
        post = self.post
        self.assertEqual(Post.get_absolute_url(post), "")


class CommentModelTest(BaseSetUp):
    def test_str_method(self):
        comment = self.comment
        self.assertEqual(Comment.__str__(comment), "Christian, was the test passing?")


class HomepageViewTest(TestCase):
    def test_page_url(self):
        response = self.client.get("/blog/")
        self.assertEqual(response.status_code, 200)

    def test_page_renders_correct_template(self):
        response = self.client.get("/blog/")
        self.assertTemplateUsed(response, "blog/blog.html")


