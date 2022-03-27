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
        def thread_function(self):
            self.ws = create_connection(f"wss://session-ws.app.senecalearning.com/?access-key={self.idToken}&sessionId={self.SessionId}")
            logging.debug(f'Connected to websocket: {self.ws.sock.server_hostname}')
            data = '{"action":"start-session","data":{"userId":"'+  self.userId +'","sessionId":"' + self.SessionId + '","courseId":"2670ac10-1d69-11e8-bf76-f14a3ef7c0e6","sectionId":"eb52d2e0-1d6b-11e8-8e43-0b8b5e91224a"}}'
            self.ws.send(data)
            logging.debug(f'Sesssion started: {self.SessionId}')
            while True:
                try:
                    data = self.ws.recv()
                    data = json.loads(data)    
                except:
                    return 
                data = data.get('data')
                TotalXp = data.get('totalXp')
                print('TotalXp: ', TotalXp )
        self.x = threading.Thread(target=thread_function, args=(self,))
        self.x.start()
        logging.debug('Thread Initiated')
        
    def End(self):
        self.ws.close()
        self.x.join()
        logging.debug('Connection closed')
        
    def SubmitData(self):
        url = "https://stats.app.senecalearning.com/api/stats/sessions"

        payload =  Create(self.SessionId)
        headers = {
            "correlationid": "1648235477567::180297b651c5a6ff4607a9288d29cdf5",
            "content-type": "application/json",
            "access-key": self.idToken,
        }

        response = requests.request("POST", url, json=payload, headers=headers)

        if response.status_code == 200:
            logging.debug('Succesful!')



