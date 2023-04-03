import uuid

from apps.accounts.managers import UserManager
from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractBaseUser):
    uuid = models.UUIDField(
        primary_key=True, db_index=True, default=uuid.uuid4, unique=True, editable=False
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    username = None
    email = models.EmailField(_("email address"), max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
