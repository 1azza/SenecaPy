from lib2to3.pgen2 import token
import requests
from pprint import pprint
from .Data.data import refresh_key ,GLOBALHEADERS
class User:
    def __init__(self, idToken):
        self.idToken = idToken

    def GetInfo(self):
        url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/getAccountInfo"

        querystring = {"key":refresh_key}

        payload = {"idToken": self.idToken}
        headers = {
            "authority": "www.googleapis.com"
        }

        response = requests.request("POST", url, json=payload, headers=headers, params=querystring)

        return response.json()

import requests








