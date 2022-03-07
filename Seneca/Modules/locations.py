import json
import json


class Locations:
    def __init__(self):
        f = open('Seneca\Modules\Data\json\Locations.json',  encoding="utf8")
        self.data = json.load(f)
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


