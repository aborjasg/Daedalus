import json
from dataclasses import asdict

from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition
from shared.models.quotes import Header, Crew

# $DaedalusSubscription = "a5cad935-1afd-4f9f-a609-9e86506f2c05"
# Format: "https://resource_name.services.ai.azure.com/api/projects/project_name"
FOUNDRY_PROJECT_ENDPOINT = "https://daedalus-project-resource.services.ai.azure.com/api/projects/daedalus-project"
# FOUNDRY_AGENT_NAME = "daedalus-agent"

# Create project and openai clients to call Foundry API
project = AIProjectClient(
    endpoint=FOUNDRY_PROJECT_ENDPOINT,
    credential=DefaultAzureCredential(),
)
openai = project.get_openai_client()

# Prepare the prompt input
header = Header("Quote for a cleaning service about a house with 2 floors and a basement", "215 8a St NE, Calgary, AB T2E 4H9", "Mr. Peter", "Vacuum Cleaning & Floor Protection Installation", Crew(2, 0, 0))
tasks = ["Vacuum Cleaning", "Floor Protection Installation"]
notes = ["Material provided by the client", "Consider hourly rate of $30 per hour for the crew", "Do not include a 5% GST in the total amount"]
output = [
    "Show details as JSON content", 
    "1) Header: Title, Property, Client, Service, Crew, Tasks, Notes", 
    "2) Details: item_number, description, crew_hours, rate, amount",
    "3) Footer: subtotal, tax_percent, tax_amount, total",
    "4) Notes: Any additional notes or disclaimers"
    ]
prompt_input = json.dumps({"header": asdict(header), "tasks": tasks, "notes": notes, "output": output})

# Run a responses API call
response = openai.responses.create(
    model="gpt-5-mini",  # supports all Foundry direct models
    input=prompt_input,
)

if not response.output_text or not response.output_text.strip():
    raise RuntimeError("Response output text was empty.")

print(f"Response output: {response.output_text}")
