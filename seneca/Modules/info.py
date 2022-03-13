import requests
from seneca.Modules.key import  APIKEY, CORRELATOINID
class Info:
    def __init__(self, idToken): 
        self.idToken = idToken
        self.headers =  {
            'access-key' : self.idToken,
        }
    def classInfo(self):
        pass
    def getAccountInfo(self):
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
        AccountInfo = response.json().get('users')[0]
        self.displayName = AccountInfo.get('displayName')
        self.email = AccountInfo.get('email')
        self.lastRefreshAt = AccountInfo.get('lastRefreshAt')
        self.passwordHash = AccountInfo.get('UkVEQUNURUQ=')
        self.photoUrl = AccountInfo.get('photoUrl')
        self.createdAt = AccountInfo.get('createdAt')
        return AccountInfo
    
    
    def getSchoolInfo(self):
        url = 'https://schools.app.senecalearning.com/api/school-info/me'
        self.headers['correlationid'] = '1647206128958::50f6180dec98105c2f1317155089ce1d'
        response = requests.request("GET", url, headers=self.headers)
        UserInfo = response.json()
        return UserInfo
    
    
    def getSubscriptionData(self):
        url = 'https://subscriptions.app.senecalearning.com/api/subscriptions/me'
        self.headers['correlationid'] = '1647206128958::50f6180dec98105c2f1317155089ce1d'
        response = requests.request("GET", url, headers=self.headers)
        SubscriptionData = response.json()
        return SubscriptionData









