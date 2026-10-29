from src.config import TEMA

from src.dominio.pokedex import (
    listar_catalogo,
    buscar_pokemon,
    mostrar_evoluciones,
    catalogo
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

from src.algoritmos.busqueda import (
    busqueda_lineal,
    busqueda_binaria
)

from src.algoritmos.ordenamiento import (
    ordenar_seleccion,
    ordenar_insercion
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


def menu_busqueda():

    print()
    print("--- Búsqueda ---")
    print("1. Búsqueda lineal")
    print("2. Búsqueda binaria")
    
    opcion_busqueda = input("> ")

    nombre = input("Nombre del Pokémon: ")

    if opcion_busqueda == "1":

        encontrado = busqueda_lineal(
            catalogo,
            nombre,
            lambda p: p.nombre
        )

    elif opcion_busqueda == "2":

        catalogo_ordenado = ordenar_insercion(
            catalogo,
            lambda p: p.nombre
        )

        encontrado = busqueda_binaria(
            catalogo_ordenado,
            nombre,
            lambda p: p.nombre
        )

    else:
        print("Opción inválida.")
        return

    if encontrado != None:
        print(f"Encontrado: {encontrado.nombre} - {encontrado.tipo}")
    else:
        print("Pokémon no encontrado.")


def menu_ordenamiento():

    print()
    print("--- Ordenamiento ---")
    print("1. Ordenar por selección")
    print("2. Ordenar por inserción")

    opcion_orden = input("> ")

    print()
    print("1. Ordenar por nombre")
    print("2. Ordenar por tipo")

    criterio = input("> ")

    if criterio == "1":
        clave = lambda p: p.nombre

    elif criterio == "2":
        clave = lambda p: p.tipo

    else:
        print("Criterio inválido.")
        return

    if opcion_orden == "1":

        resultado = ordenar_seleccion(catalogo, clave)

    elif opcion_orden == "2":

        resultado = ordenar_insercion(catalogo, clave)

    else:
        print("Opción inválida.")
        return

    print()
    print("--- Catálogo ordenado ---")

    for p in resultado:
        print(f"{p.nombre} - {p.tipo}")


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

        elif opcion == "3":

            menu_busqueda()

        elif opcion == "4":

            menu_ordenamiento()

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
