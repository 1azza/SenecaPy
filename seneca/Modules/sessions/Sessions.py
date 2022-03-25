from websocket import create_connection
import requests
import re
from seneca.Modules.sessions.data import Create

class Sessions():
    def __init__(self, idToken, SessionId):
        self.SessionId = SessionId
        self.idToken = idToken
    def Connect(self, data):
        ws = create_connection("wss://session-ws.app.senecalearning.com/?access-key=eyJhbGciOiJSUzI1NiIsImtpZCI6ImIwNmExMTkxNThlOGIyODIxNzE0MThhNjdkZWE4Mzc0MGI1ZWU3N2UiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiTGFycnkgUkVOTk9MRFNPTiIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQU9oMTRHam1BeUhtR1NrWjVQZ09wamRtUWhDRmRaclJOUTZKQzY4amRyM2F5UT1zOTYtYyIsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS9zZW5lY2EtYXV0aC1wcm9kdWN0aW9uIiwiYXVkIjoic2VuZWNhLWF1dGgtcHJvZHVjdGlvbiIsImF1dGhfdGltZSI6MTY0NzI3Nzc3OSwidXNlcl9pZCI6ImI3ZDEyZGRkLTM1ZjYtNGU0Ny1hOTg3LWZlMzY2Yjg1ZmM4NCIsInN1YiI6ImI3ZDEyZGRkLTM1ZjYtNGU0Ny1hOTg3LWZlMzY2Yjg1ZmM4NCIsImlhdCI6MTY0ODIzMTc3NSwiZXhwIjoxNjQ4MjM1Mzc1LCJlbWFpbCI6IjAxNzQzN0BicmdzbWFpbC5vcmcudWsiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJnb29nbGUuY29tIjpbIjEwNzI2Mzk3MDUzMzE5MzgxOTg2NyJdLCJlbWFpbCI6WyIwMTc0MzdAYnJnc21haWwub3JnLnVrIl19LCJzaWduX2luX3Byb3ZpZGVyIjoicGFzc3dvcmQifX0.NTsF6TIs7AeNP1HFTXsy7zDosNdZUfrpGjXRwCrIdticcfIZI0NoAICCzBYgQQEGVVTTlmA0aRtLfKbssofWcMnNO0B_9rkqVyuugCM8urWd-RgeLrO9ACF8ScA2L-McMmWDrtra6euqvMGDw94_KH0f649iCkzR-prTJmBZdvy4zFplKaeN3D2YJUFnvmhEgT43M77TOxwwQNpLXyQL-vsemtH_TsAhobhCk5oZAzpfL3-v_7w9e_hmfHyE55PaUr977BdrochwEYVbCIhVRUl9E24wB_0Fz_93Z5S_nkX45zPKQsNfYls-XjWtt-Yl72vcek7GhArUjz6sCE4cGg&sessionId=69c1fad2-918e-4640-8aea-e5c33be68bb9")
        print('Sending "action":"start-session"')
        ws.send('{"action":"start-session","data":{"userId":"b7d12ddd-35f6-4e47-a987-fe366b85fc84","sessionId":"69c1fad2-918e-4640-8aea-e5c33be68bb9","courseId":"2670ac10-1d69-11e8-bf76-f14a3ef7c0e6","sectionId":"eb52d2e0-1d6b-11e8-8e43-0b8b5e91224a"}}')
        print('Session Started')
        print("Receiving...")
        result =  ws.recv()
        print("Received '%s'" % result)
        ws.close()
        
        
        
    def SubmitData(self):
        url = "https://stats.app.senecalearning.com/api/stats/sessions"

        payload =  Create(self.SessionId)
        headers = {
            "authority": "stats.app.senecalearning.com",
            "pragma": "no-cache",
            "cache-control": "no-cache",
            "correlationid": "1648235477567::180297b651c5a6ff4607a9288d29cdf5",
            "user-region": "GB",
            "sec-ch-ua-mobile": "?0",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36",
            "content-type": "application/json",
            "access-key": self.idToken,
            "x-amz-date": "20220325T191117Z",
            "accept": "*/*",
            "origin": "https://app.senecalearning.com",
            "sec-fetch-site": "same-site",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://app.senecalearning.com/",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8"
        }

        response = requests.request("POST", url, json=payload, headers=headers)

        print(response.text)



