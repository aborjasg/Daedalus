import requests
from flask import Flask, request

app = Flask(__name__)
tenant_id = ""
client_id = ""
client_secret = ""
scope = f"api://{client_id}/ControlPanel.Manage"
authorize_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/authorize"
token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
redirect_uri = "http://localhost:5000/callback"

@app.route("/callback")
def callback():
    authorization_code = request.args.get("code")
    print("Authorization code:", authorization_code)

    if authorization_code is not None:
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

app.run(host="localhost", port=5000)