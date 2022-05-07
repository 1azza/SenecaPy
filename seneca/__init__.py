from .Modules.memories import Memories
from .Modules.token import Token
from .Modules.info import Info
from .Modules.course import Course
from .Modules.sessions import Sessions
from .Modules.profile import Profile
import logging
class User():
    '''
    A class that defines the user.
    :param username: The username of the user.
    :param password: The password of the user.
    :return: A user object.
    '''
    def __init__(self, username:str, password:str):
        token = Token(username, password)
        self.idToken = token.Refresh()
        self.info = Info(self.idToken)
        self.Username = self.info.getAccountInfo().get('displayName')
        logging.info(f'Logged in as {self.Username}')
        self.Tokens = token.userKeys
        self.id = token.user_id
        self.profile = Profile(self.idToken)
        self.memories = Memories(self.idToken)
        self.Session = Sessions
        self.profile = Profile(self.idToken)        
course = Course()