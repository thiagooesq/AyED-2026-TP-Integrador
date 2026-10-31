import time

from src.dominio.pokedex import catalogo

from src.algoritmos.busqueda import (
    busqueda_lineal,
    busqueda_binaria
)

from src.algoritmos.ordenamiento import (
    ordenar_seleccion,
    ordenar_insercion
)


def medir_tiempo(funcion, repeticiones):
    inicio = time.perf_counter()

    for i in range(repeticiones):
        funcion()

    fin = time.perf_counter()

    return (fin - inicio) / repeticiones


def ejecutar_mediciones():
    elementos = list(catalogo)

    tamanios = [
        ("Original", elementos),
        ("x10", elementos * 10),
        ("x50", elementos * 50)
    ]

    for nombre, datos in tamanios:
        print()
        print("================================")
        print("CATALOGO:", nombre)
        print("Cantidad de elementos:", len(datos))
        print("================================")

        clave = lambda p: p.nombre

        tiempo = medir_tiempo(
            lambda: busqueda_lineal(
                datos,
                "ZZZZZZZZ",
                clave
            ),
            5000
        )
        print("Busqueda lineal:", tiempo, "segundos")

        ordenados = ordenar_insercion(datos, clave)

        tiempo = medir_tiempo(
            lambda: busqueda_binaria(
                ordenados,
                "ZZZZZZZZ",
                clave
            ),
            5000
        )
        print("Busqueda binaria:", tiempo, "segundos")

        repeticiones = 10 if len(datos) == 16 else 3 if len(datos) == 160 else 1

        tiempo = medir_tiempo(
            lambda: ordenar_seleccion(datos, clave),
            repeticiones
        )
        print("Ordenamiento seleccion:", tiempo, "segundos")

        tiempo = medir_tiempo(
            lambda: ordenar_insercion(datos, clave),
            repeticiones
        )
        print("Ordenamiento insercion:", tiempo, "segundos")


if __name__ == "__main__":
    ejecutar_mediciones()
