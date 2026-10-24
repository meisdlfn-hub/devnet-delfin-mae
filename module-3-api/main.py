import requests
import json

r = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')
data = response.json()

pokemon_list = ["pikachu", "snorlax", "balbasaur", "eevee", "charmander"]

name = ["pikachu"]
height = ["3"]
weight = ["24"]

print("Who is your pokemon?")
choice = random.choice(pokemon_list)
response = response.json()


r.status_code
200
r.headers['content-type']
'application/json; charset=utf8'
r.encoding
'utf-8'
r.text
'{"authenticated": true, ...'
r.json()
{'authenticated': True, ...}


