import requests
from flask import Flask, request
from shared.http.access_token import AccessToken

tenant_id = ""
client_id =""
client_secret = ""
scope = f"api://{client_id}/ControlPanel.Manage"
authorize_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/authorize"
token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
redirect_uri = "http://localhost:5000/callback"

#access_token = AccessToken(tenant_id, client_id, client_secret, token_url, scope)
#print(access_token.get_access_token())

# auth_url = (
#     f"{authorize_url}"
#     f"?client_id={client_id}"
#     f"&response_type=code"
#     f"&redirect_uri={redirect_uri}"
#     f"&scope=api://{client_id}/ControlPanel.Manage offline_access"
#     f"&state=12345"
# )
# print("Open this URL in a browser:", auth_url)

payload = {
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret,
            "scope": f"{scope}"
        }

response = requests.post(token_url, data=payload)
response.raise_for_status()

tokens = response.json()

access_token = tokens["access_token"]
refresh_token = tokens.get("refresh_token")
print(access_token)
print(refresh_token)
