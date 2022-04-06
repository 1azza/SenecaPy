import json
from pprint import pprint
import requests
import logging

class Profile:
    '''
    This is a constructor for the class Profile.
    :param idToken: The access token for the user.
    :return: None
    '''
    def __init__(self, idToken):
        self.idToken = idToken
        self.headers = {
            "access-key": self.idToken,
            "content-type": "application/json",
            "correlationid": "1649245883892::980870b94e2a6013b6859c251e0fa7ee",
            "origin": "https://app.senecalearning.com"
        }
        
    def getAvatarId(self, name: str):  
        '''
        Gets the avatar id of the user from the avatars.app.senecalearning.com API.
        :param name: The name of the avatar.
        :return: The avatar id of the user.
        '''
        url = "https://avatars.app.senecalearning.com/api/avatars"
        response = requests.request("GET", url, headers=self.headers)
        data = response.json()
        data.get('name')
        for i in data.get('avatars'):
            if i.get('name') == name:
                return i.get('avatarId')
        logging.error('Invalid AvatarName')
        return None
    
    def setAvatar(self, AvatarId):
        '''
        Sets the avatar of the user.
        :param AvatarId: The id of the avatar.
        :return: The name of the avatar.
        '''
        url = "https://avatars.app.senecalearning.com/api/avatars"
        payload = {"avatarId": AvatarId}
        response = requests.request("POST", url, json=payload, headers=self.headers)
        AvatarName = response.json().get('name')
        return AvatarName
    def generateNewDisplayName(self):
        '''
        Generates a new display name for the user.
        :return: The new display name.
        '''
        url = "https://user-info.app.senecalearning.com/api/user-info/me/update"
        payload = {"displayName": "!generate"}
        response = requests.request("POST", url, json=payload, headers=self.headers)
        NewDisplayName = response.json().get('displayName')
        return NewDisplayName