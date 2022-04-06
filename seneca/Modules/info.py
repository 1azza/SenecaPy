from ast import Subscript
import requests
from seneca.Modules.key import  APIKEY, CORRELATOINID
class Info:
    '''
    This is a constructor for the class Info.
    :param idToken: The access key for the API.
    '''
    def __init__(self, idToken): 
        self.idToken = idToken
        self.headers =  {
            'access-key' : self.idToken,
            "origin": "https://app.senecalearning.com"
        }
    def classInfo(self):
        pass
    def getAccountInfo(self):
        '''
        Sends a GET request to the server for the user information.
        :return: The user Json object.
        '''
        """Sends a GET request to the server for the user information

        Returns:
            json: The user Json object
        """        
        url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/getAccountInfo"
        querystring = {"key": APIKEY} #We need this key otherwise we cant access the account information
        payload = {"idToken": self.idToken} #This token specifies the account we are getting the information from

        #Sending Request to get the user information
        response = requests.request("POST", url, json=payload, headers=self.headers, params=querystring)


        #Parsing Response
        AccountInfo = response.json().get('users')[0]
        self.displayName = AccountInfo.get('displayName')
        self.email = AccountInfo.get('email')
        self.lastRefreshAt = AccountInfo.get('lastRefreshAt')
        self.passwordHash = AccountInfo.get('UkVEQUNURUQ=')
        self.photoUrl = AccountInfo.get('photoUrl')
        self.createdAt = AccountInfo.get('createdAt')
        return AccountInfo
    
    def _me(self, url):
        '''
        This function is used to make a GET request to the API.
        :param url: The URL of the API.
        :return: The response of the GET request.
        '''
        self.headers['correlationid'] = '1647206128958::50f6180dec98105c2f1317155089ce1d'
        response = requests.request("GET", url, headers=self.headers)
        data = response.json()
        return data
    
    def getSchoolData(self):
        '''
        This function gets the school data from the seneca app.
        :return: A dictionary of the school data.
        '''
        url = 'https://schools.app.senecalearning.com/api/school-info/me'
        SchoolInfo =  self._me(url)
        return SchoolInfo
    
    def getUserData(self):
        '''
        This function gets the user info from the API.
        :return: A dictionary of the user info.
        '''
        url = 'https://user-info.app.senecalearning.com/api/user-info/me'
        UserInfo = self._me(url)
        return UserInfo

    
    
    def getSubscriptionData(self):
        '''
        This function gets the subscription data from the subscription API.
        :return: A dictionary of the subscription data.
        '''
        url = 'https://subscriptions.app.senecalearning.com/api/subscriptions/me'
        SubscriptionData =  self._me(url)
        return SubscriptionData
    def getKnowledgeScore(self):
        '''
        This function returns the KnowledgeScore of the user.
        :return: KnowledgeScore of the user.
        '''
        url = 'https://stats.app.senecalearning.com/api/stats/users'
        data =   self._me(url)
        sessionModulesStudied = data.get('sessionModulesStudied')
        sessionsCompleted = data.get('sessionsCompleted')
        totalStudyTime = data.get('totalStudyTime')
        KnowledgeScore = totalStudyTime*sessionsCompleted*sessionModulesStudied
        return KnowledgeScore







