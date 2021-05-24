import folium
import pandas as pd
df = pd.read_csv("in.csv")
lat = list(df["lat"])
lng = list(df["lng"])
name = list(df["city"])
pop = list(df["population_proper"])
def getColor(p):
    if p <= 5000000:
        return "green"
    elif p <= 10000000:
        return "blue"
    else:
        return "red"       
map = folium.Map(location = [20.5937,78.9629],tile = "CartoDB",zoom_start = 6)
fg = folium.FeatureGroup(name = "My Map")
for lt,lg,nm,pp in zip(lat,lng,name,pop):
    fg.add_child(folium.Marker( location=[lt,lg] , popup ="{} - {}".format(nm,pp)  , icon = folium.Icon(color = getColor(pp)) ))
#to add polygon shapes in simple line maps
fgp = folium.FeatureGroup(name = "Population")
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'})) 
map.add_child(fg)
map.add_child(fgp) 
map.add_child(folium.LayerControl()) #to add layer off/on feature
map.save("map2.html")
