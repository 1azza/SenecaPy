from pprint import pprint
import requests
from .Data.data import APIKEY ,GLOBALHEADERS
import json
import jwt                                                                                                                          
class Token:
    def __init__(self):
        pass
    def Refresh(self):
        url = "https://securetoken.googleapis.com/v1/token"
        headers = GLOBALHEADERS
        querystring = {"key": APIKEY}
        payload = "grant_type=refresh_token&refresh_token=AIwUaOmZb842ImxwkqX-GpkLq9mVzr2YrQFpfRUO6NIYKwb_byURoSy7GEHW4k7-4xIdv9QIJlMb8kK4iuMlP8FHuLnR1wACPISwN0ZJm3GJBSmmLfSjuCnEJNhcV1szMqcoemlKBf6Z74fCbR3Qknd9gBe3fp-Lj7NjCkIo4hetVq00NxvWUZcLZHlWQU2klRvloGwHLDVpR-PhlhoC9OtBZXYV3e6zIkr7-BJnrLD-iQqLAULaN9c8PK7qxIHGdJcXDpNoxKNI6TfdGYMY8nO24z80iGVh5Q"
        headers["authority"] = "securetoken.googleapis.com"
        response = requests.request(
            "POST", url, data=payload, headers=headers, params=querystring)
        self.token = response.json().get('id_token')
        print(f'New token:\n{self.token}')
        JSON = json.dumps(response.json(),   indent=4, sort_keys=True)
        with open('Seneca\\Modules\\Data\\json\\UserKeys.json', 'w',   encoding="utf8") as f:
            f.write(JSON)
        return self.token
    def DecodeToken(self):
        print('Not done yet')