import requests
from flask import Flask, request
from shared.http.access_token import AccessToken

import os


# ENV = os.getenv("APP_ENV", "dev")  # dev | test | stg | prod

# VAULT_NAME_BY_ENV = {
#     "dev": "kv-ozorasoft-daedalus",
#     "test": "kv-ozorasoft-daedalus",
#     "stg": "kv-ozorasoft-daedalus",
#     "prod": "kv-ozorasoft-daedalus",
# }

# VAULT_NAME = VAULT_NAME_BY_ENV[ENV]
# VAULT_URL = f"https://{VAULT_NAME}.vault.azure.net/"
# SECRET_NAME = "Daedalus-PrivateKey"
