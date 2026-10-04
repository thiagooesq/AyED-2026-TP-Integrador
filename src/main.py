from src.config import TEMA

from src.dominio.pokedex import (
    listar_catalogo,
    buscar_pokemon,
    mostrar_evoluciones
)

from src.dominio.equipo import Equipo
from src.dominio.historial import Historial
from src.dominio.cola_turnos import ColaTurnos

from src.excepciones import (
    ItemNoEncontradoError,
    ColeccionLlenaError,
    PilaVaciaError,
    ColaVaciaError
)


TEMAS = {
    "pokedex": "Pokédex",
    "recetario": "Recetario",
    "musica": "Biblioteca musical",
}


def mostrar_menu():
    nombre = TEMAS.get(TEMA, TEMA or "(sin tema)")

    print()
    print(f"=== {nombre} — AyED C2 2026 ===")
    print("1. Listar catálogo")
    print("2. Ver detalle")
    print("3. Buscar")
    print("4. Ordenar")
    print("5. Operación recursiva")
    print("6. Colección principal")
    print("7. Historial (pila)")
    print("8. Cola")
    print("9. Guardar / cargar archivos")
    print("0. Salir")


def menu_equipo(equipo):

    opcion = None

    while opcion != "0":

        print()
        print("--- Equipo ---")
        print("1. Agregar Pokémon")
        print("2. Listar equipo")
        print("3. Eliminar Pokémon")
        print("0. Volver")

        opcion = input("> ").strip()

        if opcion == "1":

            nombre = input("Nombre del Pokémon: ")

            try:
                p = buscar_pokemon(nombre)
                equipo.agregar(p)
                print("Pokémon agregado.")

            except ItemNoEncontradoError as e:
                print(e)

            except ColeccionLlenaError as e:
                print(e)

        elif opcion == "2":
            equipo.listar()

        elif opcion == "3":

            nombre = input("Nombre del Pokémon: ")

            try:
                p = buscar_pokemon(nombre)
                equipo.eliminar(p)
                print("Pokémon eliminado.")

            except ItemNoEncontradoError as e:
                print(e)


def menu_cola(cola_turnos):

    opcion = None

    while opcion != "0":

        print()
        print("--- Cola de turnos ---")
        print("1. Agregar turno")
        print("2. Atender siguiente turno")
        print("0. Volver")

        opcion = input("> ").strip()

        if opcion == "1":

            nombre = input("Nombre del Pokémon: ")

            try:
                p = buscar_pokemon(nombre)
                cola_turnos.agregar_turno(p)
                print("Turno agregado.")

            except ItemNoEncontradoError as e:
                print(e)

        elif opcion == "2":

            try:
                p = cola_turnos.siguiente_turno()
                print(f"Turno atendido: {p.nombre}")

            except ColaVaciaError as e:
                print(e)


def main():

    if TEMA not in TEMAS:
        print("Seteá TEMA en src/config.py: 'pokedex', 'recetario' o 'musica'.")
        return

    equipo = Equipo()
    historial = Historial()
    cola_turnos = ColaTurnos()

    opcion = None

    while opcion != "0":

        mostrar_menu()
        opcion = input("> ").strip()

        if opcion == "1":

            listar_catalogo()

        elif opcion == "5":

            nombre = input("Ingresá el nombre del Pokémon: ")

            try:
                p = buscar_pokemon(nombre)
                mostrar_evoluciones(p)
                historial.visitar(p)

            except ItemNoEncontradoError as e:
                print(e)

        elif opcion == "6":

            menu_equipo(equipo)

        elif opcion == "7":

            try:
                p = historial.deshacer()
                print(f"Deshecho: {p.nombre}")

            except PilaVaciaError as e:
                print(e)

        elif opcion == "8":

            menu_cola(cola_turnos)

        elif opcion == "0":

            print("Chau.")

        else:

            print("Opción inválida.")


if __name__ == "__main__":
    main()
