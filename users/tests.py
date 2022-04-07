from unittest import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from django.contrib.auth import get_user_model

from users.models import NewUser


class UserAccountsTest(TestCase):
    def test_super_user(self):
        db = get_user_model()
        superuser = db.objects.create_superuser(
            email="tests@gmail.com",
            role=1,
            username="userdr",
            password="password",
        )
        self.assertEqual(superuser.email, "tests@gmail.com")
        self.assertEqual(superuser.role, 1)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_active)
        self.assertEqual(str(superuser), "tests@gmail.com")

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email="email@gmail.com",
                role=1,
                username="usfer",
                password="password",
                is_superuser=False,
            )
        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email="email@gmail.com",
                role=1,
                username="usrer",
                password="password",
                is_staff=False,
            )

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email="email@gmail.com",
                role=1,
                username="usefr",
                password="password",
                is_active=False,
            )

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email="",
                role=1,
                username="user",
                password="password",
                is_superuser=True,
            )

    def test_user(self):
        db = get_user_model()
        user = db.objects.create_user(
            email="users@gmail.com",
            role=2,
            username="usert",
            password="password",
        )
        self.assertEqual(user.email, "users@gmail.com")
        self.assertEqual(user.role, 2)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertTrue(user.is_active)

        with self.assertRaises(ValueError):
            db.objects.create_user(
                email="", role=2, username="user", password="ps"
            )


class TestUserViews(APITestCase):
    def test_register_view(self):

        url = reverse("register")
        data = {
            "username": "testuser",
            "email": "test1@gmail.com",
            "password": "password",
            "role": 1,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login_view(self):

        url = reverse("login")
        user = NewUser.objects.create_user(
            email="test@gmail.com", password="password", username="lololo"
        )
        self.client.force_authenticate(user)
        data = {
            "email": "test@gmail.com",
            "password": "password",
            "username": "lololo",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)