import requests
class Info:
    def __init__(self, idToken, refresh_key): 
        """_summary_

        Args:
            idToken (str) : The user JWT created from token.refresh
        """        
        self.refresh_key = refresh_key
        self.idToken = idToken
        self.GetInfo()

    def GetInfo(self):
        """Sends a GET request to the server for the user information

        Returns:
            json: The user Json object
        """        
        url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/getAccountInfo"
        querystring = {"key":self.refresh_key} #We need this key otherwise we cant acsess the account information
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









