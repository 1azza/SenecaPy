from .Modules.memories import Memories
from .Modules.token import Token
from .Modules.info import Info
from .Modules.course import Course


class User:
    def __init__(self, username:str, password:str):
        token = Token(username, password)
        self.idToken = token.Refresh()
        self.Keys = token.userKeys
        self.id = token.user_id
        self.info = Info(self.idToken)
        self.memories = Memories(self.idToken) 
course = Course()