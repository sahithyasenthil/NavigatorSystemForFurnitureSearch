"""
Authors:
Muhammad Asghar masghar@andrew.cmu.edu 
Edvin Handoko ehandoko@andrew.cmu.edu 
Sahithya Senthilkumar sahithys@andrew.cmu.edu 
Saba Zaheer szaheer@andrew.cmu.edu
"""

from geopy.geocoders import Nominatim
from folium.plugins import MarkerCluster
import pandas as pd
import folium
import webbrowser

geolocator = Nominatim(user_agent="example app")

# Cleans the data from YellowPages
def clean_data(data):
    data["loc"] = data["Location"].apply(geolocator.geocode, timeout=10000)
    data["point"] = data["loc"].apply(lambda loc: tuple(loc.point) if loc else None)
    data = data[data['point'] != None]
    data.dropna(axis=0, inplace=True)
    data[['lat', 'lon', 'altitude']] = pd.DataFrame(data['point'].to_list(), index=data.index)
    return data

# Displays the map
def map_visualization(data):
    data = clean_data(data)
    
    # Create a map object and center it to the avarage coordinates to m
    m = folium.Map(location=data[["lat", "lon"]].mean().to_list(), zoom_start=2)

    # if the points are too close to each other, cluster them, create a cluster overlay with MarkerCluster, add to m
    marker_cluster = MarkerCluster().add_to(m)

    # draw the markers and assign popup and hover texts
    # add the markers the the cluster layers so that they are automatically clustered
    for i, r in data.iterrows():
        location = (r["lat"], r["lon"])
        folium.Marker(location=location,
                        popup = r['Name'],
                        tooltip = r['Name'])\
            .add_to(marker_cluster)

    # display the map
    m.save("mymap.html")
    webbrowser.open('mymap.html')