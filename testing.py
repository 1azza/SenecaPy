import seneca
import logging

logging.basicConfig(level=logging.DEBUG)
user = seneca.User('017437@brgsmail.org.uk', 'Larry1102')
print(user.Username)