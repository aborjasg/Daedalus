from django.http import HttpRequest, JsonResponse
from django.urls import path
from django.views.decorators.http import require_GET


@require_GET
def health(request: HttpRequest) -> JsonResponse:
    return JsonResponse({"service": "auth-api", "status": "ok"})


urlpatterns = [
    path("health", health, name="health"),
]
