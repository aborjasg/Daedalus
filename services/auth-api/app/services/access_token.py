import requests
import jwt
from pathlib import Path
from app.models.access_token import AccessToken

class AccessTokenService:

    def __init__(self):
        self.access_token = None

    def _get_public_key() -> str:
        PUBLIC_KEY_PATH = Path(__file__).with_name("daedalus-public.pem")
        with PUBLIC_KEY_PATH.open("r", encoding="utf-8") as f:
            return f.read()

    def verify_access_token(self, request):    
        public_key = self._get_public_key()
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return None

        token = auth_header.split(" ")[1]

        try:
            payload = jwt.decode(token, public_key, algorithms=["RS256"])
            
            result = {"auth_header": f"{auth_header}", "payload": payload}  
            return {"result": result }
        
        except jwt.InvalidTokenError:
            return None
        
    def get_access_token(self, access_token: AccessToken) -> str:
        self.access_token = access_token

        try:
            response = requests.post(
                self.access_token.token_url,
                data={
                    "grant_type": self.access_token.grant_type,
                    "client_id": self.access_token.client_id,
                    "client_secret": self.access_token.client_secret,
                    "scope": self.access_token.scope,
                },
            )
            response.raise_for_status()

        except requests.exceptions.RequestException as e:
            print(f"Error obtaining access token: {e}")
            return e
        
        return response


