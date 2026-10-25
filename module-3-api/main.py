import random
import requests

pokemon_list = ["pikachu", "bulbasaur", "eevee", "charmander", "squirtle"]
answer = random.choice(pokemon_list)

print("=== WHO'S THAT POKEMON? ===")

try:
    url = "https://pokeapi.co/api/v2/pokemon/" + answer
    response = requests.get(url, timeout=10)

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

        for i in range (3):
            guess = input("Enter Pokemon name: ").lower().strip()

            if guess == name:
                print("Correct! It's", name.title() + "!")
                break
            else:
                print("Wrong guess!")
        
        else:
            print("Game over! It was", name.title())

    elif response.status_code == 404:
        print("Pokemon not found!")

    else:
        print("Error:", data.status_code)

except requests.exceptions.RequestException:
    print("Please check your internet connection.")
