from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition

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

# Run a responses API call
response = openai.responses.create(
    model="gpt-5-mini",  # supports all Foundry direct models
    input="Question: What is the size of France in square miles?. Output as JSON format",
)
if not response.output_text or not response.output_text.strip():
    raise RuntimeError("Response output text was empty.")

print(f"Response output: {response.output_text}")
