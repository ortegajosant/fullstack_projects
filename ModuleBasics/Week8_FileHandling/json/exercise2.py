import json


def load_pokemons(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File not found: {file_path}, a new file will be created.")
        return []
    except json.JSONDecodeError:
        print(f"Error decoding JSON from the file: {file_path}")
        return []


def save_pokemons(file_path, pokemons):
    try:
        with open(file_path, "w") as file:
            json.dump(pokemons, file, indent=4)
    except IOError as e:
        print(f"Error saving to file: {e}")


def get_pokemon_info():
    try:
        name = input("Enter Pokémon's name: ")
        pokemon_type = input("Enter Pokémon's type: ")
        hp = int(input("Enter the Pokémon's HP: "))
        attack = int(input("Enter the Pokémon's Attack: "))
        defense = int(input("Enter the Pokémon's Defense: "))
        sp_attack = int(input("Enter the Pokémon's Special Attack: "))
        sp_defense = int(input("Enter the Pokémon's Special Defense: "))
        speed = int(input("Enter the Pokémon's Speed: "))

        return {
            "name": {"english": name},
            "type": [pokemon_type],
            "base": {
                "HP": hp,
                "Attack": attack,
                "Defense": defense,
                "Sp. Attack": sp_attack,
                "Sp. Defense": sp_defense,
                "Speed": speed,
            },
        }
    except ValueError as e:
        print(f"Invalid input: {e}")
        return None


def main():
    file_path = "pokemons.json"
    pokemons = load_pokemons(file_path)
    new_pokemon = get_pokemon_info()
    if new_pokemon:
        pokemons.append(new_pokemon)
        save_pokemons(file_path, pokemons)
        print(f"Pokémon {new_pokemon['name']['english']} added successfully.")
    else:
        print("Failed to add Pokémon.")


if __name__ == "__main__":
    main()
