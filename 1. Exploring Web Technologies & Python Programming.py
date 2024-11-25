import requests #Task2
import json

response = requests.get("https://pokeapi.co/api/v2/pokemon/jynx")
json_data = response.text

jynx_data = json.loads(json_data)

print(jynx_data["name"])
print(jynx_data["abilities"])

# Task 3
def fetch_pokemon_data(pokemon_name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
    json_data = response.text
    pokemon_data = json.loads(json_data)
    print(pokemon_data['name'])
    print(pokemon_data['abilities'])

def calculate_average_weight(pokemon_names):
    pokemon_names = ["arbok","jigglypuff","mewtwo"]
    total_weight = 0
    count = len(pokemon_names)

    for pokemon in pokemon_names:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
        json_data = response.text
        pokemon_data = json.loads(json_data)
        total_weight += pokemon_data['weight']

    average_weight = total_weight / count
    print(f"\nThe average weight of the pokemon is: {int(average_weight)}")    

fetch_pokemon_data('arbok')
fetch_pokemon_data('jigglypuff')
fetch_pokemon_data('mewtwo')

calculate_average_weight('pokemon_names')