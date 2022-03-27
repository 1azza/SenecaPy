from .Modules.memories import Memories
from .Modules.token import Token
from .Modules.info import Info
from .Modules.course import Course
from .Modules.Sessions import Sessions

class User():
    def __init__(self, username:str, password:str):
        token = Token(username, password)
        self.idToken = token.Refresh()
        self.Tokens = token.userKeys
        self.id = token.user_id
        self.info = Info(self.idToken)
        self.Username = self.info.getAccountInfo().get('displayName')
        self.memories = Memories(self.idToken)
        self.Session = Sessions

        
course = Course()