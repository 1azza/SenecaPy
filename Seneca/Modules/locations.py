import json
import requests


class Locations:
    def __init__(self):
        url = "https://memory.app.senecalearning.com/api/locations"
        querystring = {"limit":"2000"}
        headers = {"correlationid": "1647102551794::327892c76c7fed9f1443ebe7fac9c258"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        self.data = json.loads(response.text).get('items')

    def __ParseInfo(self, i):
            loc = []
            loc.append(i.get('countryName'))
            loc.append(i.get('name'))
            return loc

    def AllCountries(self):
        for i in self.data:
            print(self.__ParseInfo(i))


    def GetLocation(self, name):
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


