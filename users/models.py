from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.utils import timezone


class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, username, password, **other_fields):

        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)
        other_fields.setdefault("role", 1)

        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be assigned to is_staff=True.")
        if other_fields.get("is_superuser") is not True:
            raise ValueError(
                "Superuser must be assigned to is_superuser=True."
            )
        if other_fields.get("is_active") is not True:
            raise ValueError("Superuser must be assigned to is_active=True.")

        return self.create_user(email, username, password, **other_fields)

    def create_user(self, email, username, password, **other_fields):
        if not email:
            raise ValueError(_("You must provide an email address"))

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **other_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):
    ADMIN = 1
    CLIENT = 2
    USER_TYPE_CHOICES = ((ADMIN, "Admin"), (CLIENT, "Client"))

    email = models.EmailField(_("email address"), unique=True)
    username = models.CharField(max_length=150, unique=True)
    role = models.PositiveSmallIntegerField(
        choices=USER_TYPE_CHOICES, default=2
    )
    created_at = models.DateTimeField(default=timezone.now)
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email


class Feedback(models.Model):
    client = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    feedback = models.CharField(max_length=500)