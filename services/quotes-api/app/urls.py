import uuid

from django.http import HttpRequest, JsonResponse
from django.urls import include, path
from django.views.decorators.http import require_GET


@require_GET
def health(request: HttpRequest) -> JsonResponse:
    return JsonResponse(
        {
            "success": True,
            "data": {"service": "quotes-api", "status": "ok"},
            "errors": [],
            "correlationId": str(uuid.uuid4()),
        }
    )

endpoint_urlpatterns = [
    path("health", health, name="health"),
    # path("token", token, name="token"),
    # path("protected", protected_route, name="protected"),
]

urlpatterns = [
    path("api/v1/quotes/", include(endpoint_urlpatterns)),
]
