import requests
import sqlite3
import json

lat, lon = 45.5017, -73.5673
radius = 30000  

overpass_url = "http://overpass-api.de/api/interpreter"
query = f"""
[out:json];
(
  node["shop"="alcohol"](around:{radius},{lat},{lon});
);
out body;
"""

# data cums here into ahole (list)
response = requests.get(overpass_url, params={'data': query})
data = response.json()

# extract *moans*
liquor_stores = []
for el in data.get('elements', []):
    name = el.get('tags', {}).get('name', 'Unnamed')
    latitude = el.get('lat')
    longitude = el.get('lon')
    liquor_stores.append((name, latitude, longitude))

# first 10
print("Sample liquor stores near Montreal (50km radius):")
for store in liquor_stores[:10]:
    print(f"Name: {store[0]}, Latitude: {store[1]}, Longitude: {store[2]}")
