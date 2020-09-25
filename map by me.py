import folium
import pandas as pd

print(dir(folium))
map = folium.Map(location=[35.126411, 33.429859], zoom_start=7)
print(map)
print(dir(folium.Map))
print(map.save('test.html'))

map2 = folium.Map(location=[35.126411, 33.429859], zoom_start=15, tiles='Stamen Terrain')
print(map2)
print(map.save('test.html'))

map3 = folium.Map(location=[35.126411, 33.429859], zoom_start=15, tiles='Stamen Terrain')
print(map.save('test.html'))

map4 = folium.Map(location=[35.126411, 33.429859], zoom_start=15, tiles='Stamen Terrain')
print(map.save('Stamen Terrain'))

df = pd.read_csv('shops.txt')
def color(pop):
    if pop in range(0, 1000):
        col = 'green'
    elif pop in range(1001,1999):
        col = 'blue'
    elif pop in range(2000,2999):
        col = 'orange'
    else:
        col = 'red'
    return col

for lat,lon,name,pop in zip(df['LAT'], df['LON'], df['NAME'], df['POP']):
    folium.Marker(location=[lat, lon], popup=name, icon=folium.Icon(color = color(pop), icon = 'cloud')).add_to(map4)
print(map.save('test.html'))
