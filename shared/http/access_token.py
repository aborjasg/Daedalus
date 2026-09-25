import requests
import time
import json

class AccessToken:
    def __init__(self, tenant_id, client_id, client_secret, token_url, scope):
        self.tenant_id = tenant_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.token_url = token_url
        self.scope = scope
        self.access_token = None
        self.expiration_time = 0

    def get_access_token(self):
        current_time = time.time()
        if self.access_token is None or current_time >= self.expiration_time:
            self._refresh_access_token()
        return self.access_token


    def _refresh_access_token(self):
        self.token_url = f"https://login.microsoftonline.com/{self.tenant_id}/oauth2/v2.0/token"

        payload = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "scope": self.scope,

        }

        response = requests.post(self.token_url, data=payload)
        response.raise_for_status()

        if response.status_code == 200:
            token_data = response.json()
            self.access_token = token_data['access_token']
            expires_in = token_data.get('expires_in', 3600)  # Default to 1 hour if not provided
            self.expiration_time = time.time() + expires_in
            self.refresh_token = token_data.get("refresh_token")
        else:
            raise Exception(f"Failed to refresh access token: {response.status_code} - {response.text}")