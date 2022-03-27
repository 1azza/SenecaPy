from .Modules.memories import Memories
from .Modules.token import Token
from .Modules.info import Info
from .Modules.course import Course
from .Modules.Sessions import Sessions
import logging
class User():
    def __init__(self, username:str, password:str):
        token = Token(username, password)
        self.idToken = token.Refresh()
        self.info = Info(self.idToken)
        self.Username = self.info.getAccountInfo().get('displayName')
        logging.info(f'Logged in as {self.Username}')
        self.Tokens = token.userKeys
        self.id = token.user_id
        self.memories = Memories(self.idToken)
        self.Session = Sessions

        
course = Course()