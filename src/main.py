from src.config import TEMA
from pathlib import Path

from src.dominio.pokedex import (
    listar_catalogo,
    buscar_pokemon,
    mostrar_evoluciones,
    cargar_catalogo_inicial,
    filas_del_catalogo,
    catalogo
)

from src.persistencia.texto import guardar_texto
from src.persistencia.binario import guardar_binario

from src.dominio.equipo import Equipo
from src.dominio.historial import Historial
from src.dominio.cola_turnos import ColaTurnos

from src.excepciones import (
    ItemNoEncontradoError,
    ColeccionLlenaError,
    PilaVaciaError,
    ColaVaciaError,
    ArchivoInvalidoError
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

RUTA_DATOS = Path(__file__).resolve().parent.parent / "data"
RUTA_TXT = RUTA_DATOS / "pokedex.txt"
RUTA_BIN = RUTA_DATOS / "pokedex.bin"

ENCABEZADOS = [
    "id", "nombre", "tipo1", "tipo2",
    "hp", "ataque", "defensa",
    "velocidad", "generacion",
]

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
    print("10. Administrar catálogo (ABM)")
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

def menu_detalle():

    nombre = input("Nombre del Pokemon: ")

    try:
        p = buscar_pokemon(nombre)

        print("\n--- Detalle del pokemon ---")
        print(f"ID: {p.id}")
        print(f"Nombre: {p.nombre}")
        print(f"Tipo 1: {p.tipo1}")
        print(f"Tipo 2: {p.tipo2 or 'Ninguno'}")
        print(f"HP: {p.hp}")
        print(f"Ataque: {p.ataque}")
        print(f"Defensa: {p.defensa}")
        print(f"Velocidad: {p.velocidad}")
        print(f"Generacion: {p.generacion}")
    
    except ItemNoEncontradoError as e:
        print(e)

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


def guardar_cambios():
    guardar_texto(
        RUTA_TXT,
        filas_del_catalogo(catalogo),
        ENCABEZADOS
    )
    guardar_binario(RUTA_BIN, catalogo)


def menu_abm():
    from src.dominio.pokedex import (
        agregar_pokemon,
        eliminar_pokemon,
        modificar_pokemon
    )
    from src.dominio.pokemon import pokemon

    print("\n--- Administración del catálogo ---")
    print("1. Alta")
    print("2. Baja")
    print("3. Modificación")

    opcion = input("> ").strip()

    try:
        if opcion == "1":
            id_pokemon = int(input("ID: "))
            nombre = input("Nombre: ")
            tipo1 = input("Tipo 1: ")
            tipo2 = input("Tipo 2 (opcional): ")
            hp = int(input("HP: "))
            ataque = int(input("Ataque: "))
            defensa = int(input("Defensa: "))
            velocidad = int(input("Velocidad: "))
            generacion = int(input("Generación: "))

            nuevo = pokemon(
                nombre, tipo1, id=id_pokemon,
                tipo2=tipo2, hp=hp, ataque=ataque,
                defensa=defensa, velocidad=velocidad,
                generacion=generacion
            )

            agregar_pokemon(nuevo)
            guardar_cambios()
            print("Pokémon agregado y guardado.")

        elif opcion == "2":
            id_pokemon = int(input("ID a eliminar: "))
            eliminar_pokemon(id_pokemon)
            guardar_cambios()
            print("Pokémon eliminado y guardado.")

        elif opcion == "3":
            id_pokemon = int(input("ID a modificar: "))
            nombre = input("Nuevo nombre: ")
            tipo1 = input("Nuevo tipo 1: ")
            tipo2 = input("Nuevo tipo 2 (opcional): ")
            hp = int(input("Nuevo HP: "))
            ataque = int(input("Nuevo ataque: "))
            defensa = int(input("Nueva defensa: "))
            velocidad = int(input("Nueva velocidad: "))
            generacion = int(input("Nueva generación: "))

            modificar_pokemon(
                id_pokemon, nombre, tipo1, tipo2,
                hp, ataque, defensa, velocidad, generacion
            )
            guardar_cambios()
            print("Pokémon modificado y guardado.")

        else:
            print("Opción inválida.")

    except (ValueError, ItemNoEncontradoError,
            ArchivoInvalidoError) as error:
        print("Error:", error)

def main():

    if TEMA not in TEMAS:
        print("Seteá TEMA en src/config.py: 'pokedex', 'recetario' o 'musica'.")
        return

    ruta_datos = Path(__file__).resolve().parent.parent / "data"

    ruta_pokedex = ruta_datos / "pokedex.txt"

    try:
        cargar_catalogo_inicial(ruta_pokedex)
        print("Catálogo cargado correctamente.")

    except Exception as error:
        print("Error al cargar el catálogo:", error)
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

        elif opcion == "2":

            menu_detalle()
        
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

        elif opcion == "10":
            menu_abm ()
        
        elif opcion == "0":

            print("Chau.")

        else:

            print("Opción inválida.")


if __name__ == "__main__":
    main()
