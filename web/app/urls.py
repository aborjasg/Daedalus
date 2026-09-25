from django.http import HttpRequest, HttpResponse
from django.urls import path
from django.views.decorators.http import require_GET


@require_GET
def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Daedalus-Control Panel")


urlpatterns = [
    path("", index, name="index"),
]
