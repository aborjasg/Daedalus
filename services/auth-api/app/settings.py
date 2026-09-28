import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "local-development-only")
DEBUG = os.environ.get("DJANGO_DEBUG", "false").lower() == "true"
ALLOWED_HOSTS = [
    host
    for host in os.environ.get("DJANGO_ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")
    if host
]

ROOT_URLCONF = "app.urls"
WSGI_APPLICATION = "app.wsgi.application"
INSTALLED_APPS: list[str] = []
MIDDLEWARE: list[str] = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Secret management settings

APP_ENV = os.getenv('APP_ENV') # dev | test | stg | prod

TENANT_ID_FILE = os.getenv("TENANT_ID_FILE")
TENANT_ID = (
    Path(TENANT_ID_FILE).read_text(encoding="utf-8").rstrip("\r\n")
    if TENANT_ID_FILE
    else os.getenv("TENANT_ID")
)

CLIENT_ID_FILE = os.getenv("CLIENT_ID_FILE")
CLIENT_ID = (
    Path(CLIENT_ID_FILE).read_text(encoding="utf-8").rstrip("\r\n")
    if CLIENT_ID_FILE
    else os.getenv("CLIENT_ID")
)

CLIENT_SECRET_FILE = os.getenv("CLIENT_SECRET_FILE")
CLIENT_SECRET = (
    Path(CLIENT_SECRET_FILE).read_text(encoding="utf-8").rstrip("\r\n")
    if CLIENT_SECRET_FILE
    else os.getenv("CLIENT_SECRET")
)

SCOPE = os.getenv("SCOPE")
GRANT_TYPE = os.getenv("GRANT_TYPE")
AUTHORIZE_URL = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/authorize"
TOKEN_URL = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"
REDIRECT_URI = os.getenv("REDIRECT_URI")
