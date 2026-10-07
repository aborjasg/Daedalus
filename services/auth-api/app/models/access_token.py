import requests
import time
import json

class AccessToken:
    
    def __init__(self, token_url, client_id, client_secret, scope, grant_type):
        self.token_url = token_url
        self.client_id = client_id
        self.client_secret = client_secret        
        self.scope = scope
        self.grant_type = grant_type
        self.access_token = None
        self.expiration_time = 0

