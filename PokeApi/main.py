import requests

def getPokemonInfo(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        return data
    else:
        print(f"Falha na requisição: {response.status_code}")


pokemonName = str(input("Digite o nome de um pokémon: ")).strip().lower()
pokemonInfo = getPokemonInfo(pokemonName)

if pokemonInfo:

    print(f"Id: {pokemonInfo["id"]}")
    print(f"Nome: {pokemonInfo["name"].capitalize()}")

    i = 0
    for t in pokemonInfo["types"]:
        i+=1
        print(f"Tipo {i}: {t["type"]["name"].capitalize()}")

    print(f"Peso: {pokemonInfo["weight"]}")
    print(f"Altura: {pokemonInfo["height"]}")

