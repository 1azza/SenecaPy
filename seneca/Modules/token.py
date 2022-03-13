from pprint import pprint
import requests
import json
class Token:
    def __init__(self):
        pass
    
    def Refresh(self, refresh_key):
        """
        Args:
            token (str): Your User refresh_token
        Returns:
            string: Updated id_token (json web token)
        """        
        url = "https://securetoken.googleapis.com/v1/token"
        headers = {}
        querystring = {"key": refresh_key}
        payload = "grant_type=refresh_token&refresh_token=AIwUaOmZb842ImxwkqX-GpkLq9mVzr2YrQFpfRUO6NIYKwb_byURoSy7GEHW4k7-4xIdv9QIJlMb8kK4iuMlP8FHuLnR1wACPISwN0ZJm3GJBSmmLfSjuCnEJNhcV1szMqcoemlKBf6Z74fCbR3Qknd9gBe3fp-Lj7NjCkIo4hetVq00NxvWUZcLZHlWQU2klRvloGwHLDVpR-PhlhoC9OtBZXYV3e6zIkr7-BJnrLD-iQqLAULaN9c8PK7qxIHGdJcXDpNoxKNI6TfdGYMY8nO24z80iGVh5Q"
        headers = {
            "authority": "securetoken.googleapis.com",
            "pragma": "no-cache",
            "cache-control": "no-cache",
            "content-type": "application/x-www-form-urlencoded",
            "x-client-version": "Chrome/JsCore/8.4.0/FirebaseCore-web",
            "sec-ch-ua-mobile": "?0",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
            "accept": "*/*",
            "origin": "https://app.senecalearning.com",
            "x-client-data": "CIu2yQEIpLbJAQjEtskBCKmdygEIjtLKAQie+csBCOaEzAEImpzMAQ==",
            "sec-fetch-site": "cross-site",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://app.senecalearning.com/",
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
    def DecodeToken(self):
        print('Not done yet')
        