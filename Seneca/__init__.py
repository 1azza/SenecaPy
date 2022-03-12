from .Modules.locations import Locations
from .Modules.token import Token
from .Modules.info import Info
from .Modules.answers import Answers


class User:
    def __init__(self, Refresh_key):
        token = Token()
        self.idToken = token.Refresh(Refresh_key)
        self.Keys = token.userKeys
        self.id = token.user_id
        self.info = Info(self.idToken, Refresh_key)

locations = Locations() 
answers = Answers()