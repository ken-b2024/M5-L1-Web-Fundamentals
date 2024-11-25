import requests

def fetch_planet_data():
    response = requests.get('https://api.le-systeme-solaire.net/rest/bodies/')
    planets = response.json()['bodies']

    planet_data = []
    for planet in planets:
        if planet['isPlanet']:  # Only consider planets
            orbit_period = planet['sideralOrbit']
            if orbit_period:  # Only include planets with an orbit period
                planet_data.append({
                    'name': planet['englishName'],
                    'orbit_period': orbit_period
                })
    return planet_data
            
def find_longest_orbit_period(planets):
    max_orbit = 0
    longest_orbit_planet = None
    
    for planet in planets:
        if planet['orbit_period'] > max_orbit:
            max_orbit = planet['orbit_period']
            longest_orbit_planet = planet['name']
    return longest_orbit_planet, max_orbit

planets = fetch_planet_data()
name, orbit_period = find_longest_orbit_period(planets)

if name and orbit_period:
    print(f"\nThe planet with the longest orbital time is {name} with an orbit of {orbit_period} days")