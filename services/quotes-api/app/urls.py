import json
import uuid
from dataclasses import asdict

from django.http import HttpRequest, JsonResponse
from django.urls import include, path
from django.views.decorators.http import require_GET, require_POST
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from shared.models.quotes import Crew, Header

# Format: "https://resource_name.services.ai.azure.com/api/projects/project_name"
FOUNDRY_PROJECT_ENDPOINT = "https://daedalus-project-resource.services.ai.azure.com/api/projects/daedalus-project"

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

@require_GET
def generation(request: HttpRequest) -> JsonResponse:
    # Create project and openai clients to call Foundry API
    project = AIProjectClient(
        endpoint=FOUNDRY_PROJECT_ENDPOINT,
        credential=DefaultAzureCredential(),
    )
    openai = project.get_openai_client()


    # Prepare the prompt input
    header = Header("Quote for a cleaning service", "215 8a St NE, Calgary, AB T2E 4H9", "Mr. Peter", "Vacuum Cleaning & Floor Protection Installation", Crew(2, 0, 0))
    tasks = ["Vacuum Cleaning", "Floor Protection Installation", "Material provided by the contractor"]
    prompt_input = json.dumps({"header": asdict(header), "tasks": tasks})

    # Run a responses API call
    response = openai.responses.create(
        model="gpt-5-mini",  # supports all Foundry direct models
        input=prompt_input,
    )

    if not response.output_text or not response.output_text.strip():
        raise RuntimeError("Response output text was empty.")

    # Here you would implement the logic to generate a quote based on the request data.
    # For now, we'll return a placeholder response.
    return JsonResponse(
        {
            "success": True,
            "data": {"quote": response.output_text},
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
