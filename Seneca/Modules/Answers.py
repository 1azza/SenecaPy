from lib2to3.pgen2 import token
import requests
from pprint import pprint
from .Data.data import refresh_key ,GLOBALHEADERS
class Answers:
    def __init__(self, idToken):
        self.idToken = idToken


    def _parseUrl(self):
        courseId = self.url.split('course/')[1].split('/section')[0]
        SectionId = self.url.split('section/')[1].split('/session')[0]
        return [courseId, SectionId]

    def Get(self, url):
        Template = ['https://course.app.senecalearning.com/api/courses/', '/signed-url']
        self.url = url
        Ids = self._parseUrl()[0]
        Template.insert(1, Ids)
        print(Template)
        self.url = ''.join(Template)
        print(self.url)
        querystring = {"sectionId":"e7302180-1d3a-11e8-826e-91b9b920c8af"}
        headers = {
            "authority": "course.app.senecalearning.com",
            "correlationid": "1646689150102::d1ad61f3c3f3a08c484a352cbf79c72d",
        }
        response = requests.request("GET", self.url, headers=headers, params=querystring)

        print(response.text)

import requests








