import os
from pathlib import Path
from app.controllers.access_token import get_access_token

from django.http import HttpRequest, JsonResponse
from django.urls import path
from django.views.decorators.http import require_GET, require_POST

APP_ENV = os.getenv('APP_ENV')

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
AUTHORIZE_URL = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/authorize"
TOKEN_URL = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"
REDIRECT_URI = os.getenv("REDIRECT_URI")


@require_GET
def health(request: HttpRequest) -> JsonResponse:
    return JsonResponse({"service": "auth-api", "endpoint": "health", "status": "ok"})


@require_GET
def access_token(request: HttpRequest) -> JsonResponse:
    print(f"Client ID: {CLIENT_ID}")
    token = get_access_token(
        CLIENT_ID,
        CLIENT_SECRET,
        SCOPE,
        TOKEN_URL,
    )
    # print(f"Access Token: {token}")
    return JsonResponse({"service": "auth-api", "endpoint": "access_token", "status": "ok", "params":f"{APP_ENV} | {SCOPE} | {TOKEN_URL}", "response": f"{token}"})


urlpatterns = [
    path("health", health, name="health"),
    path("access_token", access_token, name="access_token"),
]
