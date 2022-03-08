from pprint import pprint
import Seneca

token = Seneca.token.Refresh('AIzaSyDXmCdeFZFJbQOtl6xupkxZw-lIOKuJQKg')
user = Seneca.User(token)

Seneca.answers.Fetch('https://app.senecalearning.com/classroom/course/f4a9de91-3dcc-4e19-b180-1286357dded5/section/2d349e50-8362-4aba-b189-6f376c86b577/session')