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

# Prepare dependencies for pip

```
mkdir requirements
touch requirements/{base,dev,test,prod}.txt
pip freeze >! requirements/base.txt
```
