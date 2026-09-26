import requests

def get_access_token(client_id: str, client_secret: str, scope: str, token_url: str) -> str:
    try:
        response = requests.post(
            token_url,
            data={
                "grant_type": "client_credentials",
                "client_id": client_id,
                "client_secret": client_secret,
                "scope": scope,
            },
        )
        response.raise_for_status()

    except requests.exceptions.RequestException as e:
        print(f"Error obtaining access token: {e}")
        return e

    tokens = response.json()
    
    return tokens