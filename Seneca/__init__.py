from .Modules.locations import Locations
from .Modules.token import Token
from .Modules.Data.data import refresh_key
from .Modules.user import User
from .Modules.info import Info
from .Modules.answers import Answers

token = Token()
if token.Refresh(refresh_key) == 0:
    print('Enter new token in Seneca\Modules\Data\data.py')

locations = Locations() 
user = User(token.idToken)
info =Info(token.idToken)
answers = Answers(token.idToken)