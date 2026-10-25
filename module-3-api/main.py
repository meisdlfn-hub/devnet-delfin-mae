
import random

pokemon_list = ["pikachu", "bulbasaur", "eevee", "charmander", "squirtle"]
answer = random.choice(pokemon_list)

print("=== WHO'S THAT POKEMON? ===")

guess = input("Enter Pokemon name: ").lower().strip()

if guess == answer:
    print("Correct! It's", answer.title() + "!")
else:
    print("Wrong! The Pokemon was", answer.title())
