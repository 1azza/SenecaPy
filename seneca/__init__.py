from .Modules.locations import Locations
from .Modules.token import Token
from .Modules.info import Info
from .Modules.answers import Answers


class User:
    def __init__(self, username, password):
        token = Token(username, password)
        self.idToken = token.Refresh()
        self.Keys = token.userKeys
        self.id = token.user_id
        self.info = Info(self.idToken)

locations = Locations() 
answers = Answers()