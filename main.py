import Seneca
import folium
Coords = Seneca.locations.GetLocation('Rio')
m = folium.Map(location=Coords, 
                zoom_start=4, control_scale=True, prefer_canvas=True)
folium.Marker(
    location=Coords,
    popup=Seneca.locations.name,
    icon=folium.Icon(color='green', icon='ok-sign')
).add_to(m)
m.save('map.html')