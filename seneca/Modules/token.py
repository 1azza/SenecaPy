from pprint import pprint
import requests
from seneca.Modules.key import  APIKEY
import json
class Token:
    def __init__(self,  email:str, password:str):
        url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword"

        querystring = {"key": APIKEY}

        payload = {
            "email": email,
            "password": password,
            "returnSecureToken": True
        }
        self.headers = {
            "authority": "www.googleapis.com",
            "pragma": "no-cache",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
        }

        response = requests.request("POST", url, json=payload, headers=self.headers, params=querystring)

        self.refereshToken = response.json().get('refreshToken')

        
    def Refresh(self):
        url = "https://securetoken.googleapis.com/v1/token"
        querystring = {"key": APIKEY}
        payload = f"grant_type=refresh_token&refresh_token={self.refereshToken}"
        headers = {
            "authority": "securetoken.googleapis.com",
            "pragma": "no-cache",
            "cache-control": "no-cache",
            "content-type": "application/x-www-form-urlencoded",
            "x-client-version": "Chrome/JsCore/8.4.0/FirebaseCore-web",
            "sec-ch-ua-mobile": "?0",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
            "accept": "*/*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8"
        }

        response = requests.request(
            "POST", url, data=payload, headers=headers, params=querystring)
        self.idToken = response.json().get('id_token')
        self.user_id = response.json().get('user_id')
        if self.idToken == None:
            print(response)
        else:
            self.userKeys = json.dumps(response.json(),   indent=4, sort_keys=True)
            return self.idToken
        