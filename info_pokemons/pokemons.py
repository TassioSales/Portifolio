#criar app que recebe um pokemon e retorna suas informações
#acessar a api  https://pokeapi.co/api/v2/pokemon/{}

import requests
import json

def main():
    pokemon = input("Digite o nome do pokemon: ")
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    response = requests.get(url)
    data = json.loads(response.text)
    print(f"Nome: {data['name']}")
    print(f"Altura: {data['height']}")
    print(f"Peso: {data['weight']}")
    print(f"Tipo: {data['types'][0]['type']['name']}")
    print(f"Habilidades: {data['abilities'][0]['ability']['name']}")
    print(f"Experiência base: {data['base_experience']}")
    print(f"Ordem: {data['order']}")
    print(f"ID: {data['id']}")
    print(f"Imagem: {data['sprites']['front_default']}")
    print(f"Imagem: {data['sprites']['back_default']}")
    print(f"Imagem: {data['sprites']['front_shiny']}")
    print(f"Imagem: {data['sprites']['back_shiny']}")


if __name__ == "__main__":
    main()
