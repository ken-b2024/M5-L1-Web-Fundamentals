import requests

#Task 2
def fetch_planet_data():
    response = requests.get('https://api.le-systeme-solaire.net/rest/bodies/')
    planets = response.json()['bodies']

    for planet in planets:
        if planet['isPlanet']:
            name = planet['englishName']
            mass = planet['mass']['massValue']
            orbit_period = planet['sideralOrbit']
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

fetch_planet_data()