import requests
from seneca.Modules.key import  APIKEY
class Info:
    def __init__(self, idToken): 
        self.idToken = idToken
        self.GetInfo()

    def GetInfo(self):
        """Sends a GET request to the server for the user information

        Returns:
            json: The user Json object
        """        
        url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/getAccountInfo"
        querystring = {"key": APIKEY} #We need this key otherwise we cant acsess the account information
        payload = {"idToken": self.idToken} #This token specifies the account we are getting the information from
        headers = {
            "authority": "www.googleapis.com"
        }
        #Sending Request to get the user information
        response = requests.request("POST", url, json=payload, headers=headers, params=querystring)


        #Parsing Response
        userData = response.json().get('users')[0]
        self.displayName = userData.get('displayName')
        self.email = userData.get('email')
        self.lastRefreshAt = userData.get('lastRefreshAt')
        self.passwordHash = userData.get('UkVEQUNURUQ=')
        self.photoUrl = userData.get('photoUrl')
        self.createdAt = userData.get('createdAt')



        return userData









