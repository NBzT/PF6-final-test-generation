import json
import requests


def buscar_dish(numero):

    response = requests.get("https://api-colombia.com/api/v1/TypicalDish")
    dishes = json.loads(response.content)


    for dish in dishes:
        if dish.get('id') == numero:
          return {
        "id": dish.get('id'),
        "name": dish.get('name'),
        "description": dish.get('description'),
            }
    return

##________________________________________________________##
def main():
    print("Hello learners! Welcome to Colombia!")


    print("Escoja el plato típico de su gusto\n")

    try:
        numero = int(input("Escoja su plato favorito ingresando un número del 1 al 68"))
        info = buscar_dish(numero)
        if info:
            print("\nInformación de su plato escogido:")
            for key, value in info.items():
                print(f"{key.capitalize()}: {value}")
        else:
            print("Ingrese un valor del 1 al 68")
    except ValueError:
        print("Por favor ingrese un número válido.")

if __name__ == "__main__":
    main()