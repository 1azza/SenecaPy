import json
from pprint import pprint
import requests


class Memories:
    '''
    This class is used to store the data from the memory app.
    :param idToken: The token used to access the data.
    :return: None
    '''
    def __init__(self, idToken):
        self.idToken = idToken
        url = "https://memory.app.senecalearning.com/api/locations"
        querystring = {"limit":"2000"}
        headers = {"correlationid": "1647102551794::327892c76c7fed9f1443ebe7fac9c258"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        self.data = json.loads(response.text).get('items')

    def __ParseInfo(self, i):
        '''
        Parses the information from the json file and returns a list of the required information.
        :param i: The information from the json file.
        :return: A list of the required information.
        '''
        loc = []
        loc.append(i.get('countryName'))
        loc.append(i.get('name'))
        loc.append(i.get('id'))
        return loc

    def AllCountries(self):
        '''
        This function returns a list of all the countries in the dataset.
        :return: A list of all the countries in the dataset.
        '''
        Countries = []
        for i in self.data:
            Countries.append((self.__ParseInfo(i)))
        return Countries
    def SetMemory(self, courseId, sectionId, locationId, courseName ,sectionTitle):
        '''
        Sets a memory in the Seneca Learning Memory API.
        :param courseId: The course ID of the course.
        :param sectionId: The section ID of the section.
        :param locationId: The location ID of the location.
        :param courseName: The name of the course.
        :param sectionTitle: The title of the section.
        :return: None
        '''
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
        '''
        Gets the location of a location.
        :param name: The name of the location.
        :return: The latitude and longitude of the location.
        '''
        for i in self.data:
            if i.get('name') == name:
                print('Found Location for:')
                self.name = print(self.__ParseInfo(i))
                Coords = []
                Coords.append(i.get('latitude'))
                Coords.append(i.get('longitude'))

                return Coords


