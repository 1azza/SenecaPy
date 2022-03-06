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
        for i in self.data:
            if i.get('name') == name:
                print('Found Location for:')
                self.name = print(self.__ParseInfo(i))
                l = []
                l.append(i.get('latitude'))
                l.append(i.get('longitude'))

                return l


