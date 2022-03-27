from websocket import create_connection
import requests
from seneca.Modules.data import Create
import threading
from pprint import pprint
import json
import logging
class Sessions():
    def __init__(self,  SessionId, User):
        self.SessionId = SessionId
        self.idToken = User.idToken
        self.userId = User.id
        
    def Start(self):
        self.ws = create_connection(f"wss://session-ws.app.senecalearning.com/?access-key={self.idToken}&sessionId={self.SessionId}")
        logging.info('Connected to websocket')
        data = '{"action":"start-session","data":{"userId":"'+  self.userId +'","sessionId":"' + self.SessionId + '","courseId":"2670ac10-1d69-11e8-bf76-f14a3ef7c0e6","sectionId":"eb52d2e0-1d6b-11e8-8e43-0b8b5e91224a"}}'
        logging.info('Starting session')
        self.ws.send(data)
        logging.info("Session ready")
        def thread_function(self):
            while True:
                data = self.ws.recv()
                try:
                    data = json.loads(data)
                except:
                    break
                data = data.get('data')
                TotalXp = data.get('totalXp')
                print('TotalXp: ', TotalXp )
        x = threading.Thread(target=thread_function, args=(self,))
        x.start()
        
    def End(self):
        self.ws.close()
        
        
        
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

        if response.status_code == 200:
            pass



