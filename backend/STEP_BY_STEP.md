# Create a virtual environment

```python
python3 -m venv .venv
python3 -m pip install --upgrade pip
```

# Install Django

```python
pip install django==4.2
pip install djangorestframework==3.14.0
```

# Start a new project

```python
mkdir -p backend
cd backend
django-admin startproject core .
```

Structure:

```
├── STEP_BY_STEP.md
├── core
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py

```

# Prepare setting files

Update file `core/settings.py`

```
import os
SECRET_KEY = os.environ.get("SECRET_KEY", "my-secret-key")
DEBUG = bool(int(os.environ.get("DEBUG", "1")))
```

Change settings to multiple environment files:

```bash
mkdir -p core/settings
mv core/settings.py core/settings/base.py
touch core/settings/__init__.py
touch core/settings/{development,test,staging,production}.py
echo "from .base import *  # noqa" >> core/settings/development.py
```

Update file `core/settings/base.py` (add `.parent`)

```
BASE_DIR = Path(__file__).resolve().parent.parent.parent
```

Update `DJANGO_SETTINGS_MODULE` in file `manage.py`

```
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.development")
```

# Split installed apps

Update file `core/settings/base.py` like this:

```
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
]

LOCAL_APPS = [
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
```

# Prepare dependencies for pip

```
mkdir requirements
touch requirements/{base,dev,test,prod}.txt
pip freeze >! requirements/base.txt
```

# Create a new app named `common`

```bash
mkdir -p apps/common
django-admin startapp common ./apps/common
```

Update file `apps/common/apps.py`

```
name = "apps.common"
```

Update file `core/settings/base.py` like this:

```
LOCAL_APPS = [
    "apps.common",
]
```

# Create a common model

```bash
mkdir -p apps/common/models
mv apps/common/models.py apps/common/models/base.py
echo "from .base import BaseModel" > apps/common/models/__init__.py
```

Add the following content to `apps/common/models/base.py`

```python
import uuid

from django.conf import settings
from django.db import models


class BaseModel(models.Model):
    uuid = models.UUIDField(
        primary_key=True, db_index=True, default=uuid.uuid4, unique=True, editable=False
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        default=None,
        blank=True,
        editable=False,
        on_delete=models.SET_NULL,
        related_name="%(class)s_created_by",
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        default=None,
        blank=True,
        editable=False,
        on_delete=models.SET_NULL,
        related_name="%(class)s_updated_by",
    )

    class Meta:
        abstract = True
```

- We will use `uuid` for primary key for all models.
- We also prepare some common fields: `created_at`, `updated_at`, `created_by`, `updated_by` to tracking the value of each record.

# Create a new app named `accounts`

```bash
mkdir -p apps/accounts
django-admin startapp accounts ./apps/accounts
```

Update file `apps/accounts/apps.py`

```
name = "apps.accounts"
```

Update file `core/settings/base.py` like this:

```
LOCAL_APPS = [
    "apps.accounts",
]
```

# Customize User model

```bash
mkdir -p apps/accounts/models
mv apps/accounts/models.py apps/accounts/models/user.py
echo "from .user import User" > apps/accounts/models/__init__.py
mkdir -p apps/accounts/managers
echo "from .user import UserManager" > apps/accounts/managers/__init__.py
touch apps/accounts/managers/user.py
```

Add the following content to `apps/accounts/managers/user.py`

```python
from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, password):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Create and save a SuperUser with the given email and password.
        """
        user = self.create_user(email, password)
        user.is_admin = True
        user.save(using=self._db)
        return user
```

Add the following content to `apps/accounts/models/user.py`

```python
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
```

Add the following content to `core/settings/base.py`

```python
# Customize user model
AUTH_USER_MODEL = "accounts.User"
```

From now, we can make migrations and migrate.

```bash
./manage.py makemigrations
./manage.py migrate
```