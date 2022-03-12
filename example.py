from pprint import pprint
import seneca



#Get answers from a course session url
seneca.answers.Fetch('https://app.senecalearning.com/classroom/course/f4a9de91-3dcc-4e19-b180-1286357dded5/section/2d349e50-8362-4aba-b189-6f376c86b577/session')


#Get exact location from a place name from seneca
pprint(seneca.locations.GetLocation('San Pedro de Atacama'))




#Initialise user object
user = seneca.User('AIzaSyDXmCdeFZFJbQOtl6xupkxZw-lIOKuJQKg')


#Get All keys stored within the account
pprint(user.Keys)


#Get information stored within the  account
pprint(user.info.GetInfo())






