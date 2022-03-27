from pprint import pprint
import requests
from seneca.Modules.key import  APIKEY
import json
from seneca.Modules.errors import (ServerError, InvalidCredentials)
import logging
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
        logging.info(f'Logging in as: {email}')
        response = requests.request("POST", url, json=payload, headers=self.headers, params=querystring)
        self.refereshToken = response.json().get('refreshToken')
        if response.status_code == 400:
            raise InvalidCredentials()
        elif response.status_code != 200:
            raise ServerError()
        
    def Refresh(self):
        url = "https://securetoken.googleapis.com/v1/token"
        querystring = {"key": APIKEY}
        payload = f"grant_type=refresh_token&refresh_token={self.refereshToken}"
        headers = {
            "content-type": "application/x-www-form-urlencoded",
        }
        response = requests.request(
            "POST", url, data=payload, headers=headers, params=querystring)
        if response.status_code == 200:
            logging.info('Refreshed idToken')
        elif response.status_code == 400:
            raise InvalidCredentials()
        else:
            raise ServerError()
            
        self.idToken = response.json().get('id_token')
        self.user_id = response.json().get('user_id')
        
        if self.idToken == None:
            logging.critical('No idToken found')
        else:
            self.userKeys = json.dumps(response.json(),   indent=4, sort_keys=True)
            return self.idToken
        