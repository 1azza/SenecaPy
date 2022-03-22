import json
from pprint import pprint
import requests


class Memories:
    def __init__(self, idToken):
        self.idToken = idToken
        url = "https://memory.app.senecalearning.com/api/locations"
        querystring = {"limit":"2000"}
        headers = {"correlationid": "1647102551794::327892c76c7fed9f1443ebe7fac9c258"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        self.data = json.loads(response.text).get('items')

    def __ParseInfo(self, i):
            loc = []
            loc.append(i.get('countryName'))
            loc.append(i.get('name'))
            loc.append(i.get('id'))
            return loc

    def AllCountries(self):
        Countries = []
        for i in self.data:
            Countries.append((self.__ParseInfo(i)))
        return Countries
    def SetMemory(self, courseId, sectionId, locationId, courseName ,sectionTitle):
        url = "https://memory.app.senecalearning.com/api/memories"

        payload = {
            "courseId": courseId,
            "courseName": courseName,
            "sectionId": sectionId,
            "sectionTitle": sectionTitle,
            "locationId": locationId,
            "timeEarned": "2022-03-21T17:55:31+00:00"
        }
        headers = {
            "correlationid": "1647885342893::8fb5230c62f1c5be3acec6582830e7b5",
            "access-key": self.idToken,
        }

        response = requests.request("POST", url, json=payload, headers=headers)
        if response.status_code == 201:
            print(response)
            print('Set!')
            pprint(response.json().get('courseName'))
        else:
            print('Error')
            pprint(response.json())

        

    def GetLocation(self, name:str):
        """
        Finds Longitude and Latitude coords from the name of the location from seneca
        Args:
            name (string): The name of the place to find

        Returns:
            Coords (list): Longitude and Latidud of the location
        """                
        for i in self.data:
            if i.get('name') == name:
                print('Found Location for:')
                self.name = print(self.__ParseInfo(i))
                Coords = []
                Coords.append(i.get('latitude'))
                Coords.append(i.get('longitude'))

                return Coords


