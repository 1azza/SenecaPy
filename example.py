from pprint import pprint
import Seneca

token = Seneca.token.Refresh('AIzaSyDXmCdeFZFJbQOtl6xupkxZw-lIOKuJQKg')
user = Seneca.User(token)

Seneca.answers.Fetch('https://app.senecalearning.com/classroom/course/9b389a80-1cb0-11e8-ba7f-85cc3dd82400/section/f2113da0-1cb3-11e8-ba7f-85cc3dd82400/session')