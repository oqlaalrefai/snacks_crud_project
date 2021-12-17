from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Snack
# Create your tests here.


class SnackTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass"
        )

        self.Snack = Snack.objects.create(
            title="shawarma", purchaser=self.user, description="tastey chicken sandwich",
        )

    def test_string_representation(self):
        self.assertEqual(str(self.Snack), "shawarma")

    def test_snack_content(self):
        self.assertEqual(f"{self.Snack.title}", "shawarma")
        self.assertEqual(f"{self.Snack.purchaser}", "tester")
        self.assertEqual(self.Snack.description, "tastey chicken sandwich")

    def test_snack_list_view(self):
        response = self.client.get(reverse("snacks"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "shawarma")
        self.assertTemplateUsed(response, "snack_list.html")

    def test_snack_detail_view(self):
        response = self.client.get(reverse("snack_detail", args="1"))
        no_response = self.client.get("/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Purchaser: tester")
        self.assertTemplateUsed(response, "snack_detail.html")

    def test_snack_create_view(self):
        response = self.client.post(
            reverse("snack_create"),
            {
                "title": "kebab",
                "purchaser": self.user.id,
                "description": "meat sandwich",
            }, follow=True
        )

        self.assertRedirects(response, reverse("snack_detail", args="2"))
        self.assertContains(response, "Title:")



    def test_Snack_update_view_redirect(self):
        response = self.client.post(
            reverse("snack_update", args="1"),
            {"title": "Updated title","purchaser":self.user.id,"description":"taste food"}
        )

        self.assertRedirects(response, reverse("snack_detail", args="1"))

    def test_Snack_delete_view(self):
        response = self.client.get(reverse("snack_delete", args="1"))
        self.assertEqual(response.status_code, 200)