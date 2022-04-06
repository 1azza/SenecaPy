import json
from pprint import pprint
import requests


class Profile:
    def __init__(self, idToken):
        self.idToken = idToken
    def getAvatarId(self, name: str):
        url = "https://avatars.app.senecalearning.com/api/avatars"
        headers = {
            "access-key": self.idToken,
            "content-type": "application/json",
            "correlationid": "1649245883892::980870b94e2a6013b6859c251e0fa7ee"
        }
        response = requests.request("GET", url, headers=headers)
        data = response.json()
        data.get('name')
        for i in data.get('avatars'):
            if i.get('name') == name:
                return i.get('avatarId')
        return None
    
    def setAvatar(self, AvatarId):
        url = "https://avatars.app.senecalearning.com/api/avatars"
        payload = {"avatarId": AvatarId}
        headers = {
            "accept": "*/*",
            "access-key": "eyJhbGciOiJSUzI1NiIsImtpZCI6IjZhNGY4N2ZmNWQ5M2ZhNmVhMDNlNWM2ZTg4ZWVhMGFjZDJhMjMyYTkiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiTGFycnkgUkVOTk9MRFNPTiIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQU9oMTRHam1BeUhtR1NrWjVQZ09wamRtUWhDRmRaclJOUTZKQzY4amRyM2F5UT1zOTYtYyIsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS9zZW5lY2EtYXV0aC1wcm9kdWN0aW9uIiwiYXVkIjoic2VuZWNhLWF1dGgtcHJvZHVjdGlvbiIsImF1dGhfdGltZSI6MTY0ODM5NjUyMywidXNlcl9pZCI6ImI3ZDEyZGRkLTM1ZjYtNGU0Ny1hOTg3LWZlMzY2Yjg1ZmM4NCIsInN1YiI6ImI3ZDEyZGRkLTM1ZjYtNGU0Ny1hOTg3LWZlMzY2Yjg1ZmM4NCIsImlhdCI6MTY0OTI0NTczMSwiZXhwIjoxNjQ5MjQ5MzMxLCJlbWFpbCI6IjAxNzQzN0BicmdzbWFpbC5vcmcudWsiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJnb29nbGUuY29tIjpbIjEwNzI2Mzk3MDUzMzE5MzgxOTg2NyJdLCJlbWFpbCI6WyIwMTc0MzdAYnJnc21haWwub3JnLnVrIl19LCJzaWduX2luX3Byb3ZpZGVyIjoiZ29vZ2xlLmNvbSJ9fQ.wHa3Gd3W7EHGRzl1q0FZccBO-HFaDHwMt0jomvY_u1Uf67XAy6xMKDidsBMeUUPJczX5-8P2z47jpGkFGYvHwRehD6of1A2hju-RChFlNEWWLLLX89vGHjbcdUCJg3O7II2V_SENdcDhHDD8uVYuD5LatfPcITZPdtyqtuL2Dy0geVCDC1GvsVSiZNtAIQTKmb394ANsJM1gn9CsOPA48mvj9zmJVTc_jPzBjODoiyVVxO5QvM0iZbapxLi4jzfD4zmb5760FUADB-uWQ6vFBc776Gjq9SGTnZyFOaot7SplDzmtEUFErDtdrjiQAx_ymuPO8lhhgFQvfMLMiFk_dA",
            "content-type": "application/json",
            "correlationid": "1649245905742::e3401a891cfd16c707d4b9de29607e57",
        }

        response = requests.request("POST", url, json=payload, headers=headers)
        print(response.json())
