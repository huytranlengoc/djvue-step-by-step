import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from users.managers import UserManager


class User(AbstractUser):
    uuid = models.UUIDField(
        primary_key=True, db_index=True, default=uuid.uuid4, unique=True, editable=False
    )

    username = None
    email = models.EmailField(_("email address"), max_length=255, unique=True)
    first_name = models.CharField(_("first name"), max_length=150)
    last_name = models.CharField(_("last name"), max_length=150)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        db_table = "users"

    def __str__(self):
        return self.email
