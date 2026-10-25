import random
import requests

pokemon_list = ["pikachu", "bulbasaur", "eevee", "charmander", "squirtle"]
answer = random.choice(pokemon_list)

print("=== WHO'S THAT POKEMON? ===")

url = "https://pokeapi.co/api/v2/pokemon/" + answer
response = requests.get(url)

if response.status_code == 200:
    info = response.json()

    name = info["name"]
    height = info["height"]
    weight = info["weight"]
    ability = info["abilities"][0]["ability"]["name"]

    print("\nGuess the Pokemon!")
    print("Height:", info["height"])
    print("Weight:", info["weight"])
    print("Ability:", ability.replace("-", " ").title())

    guess = input("Enter Pokemon name: ").lower().strip()

    if guess == info["name"]:
        print("Correct! It's", info["name"].title() + "!")
    else:
        print("The Pokemon was", info["name"].title())

elif response.status_code == 404:
    print("Pokemon not found!")

else:
    print("Request failed. Status:", response.status_code)
