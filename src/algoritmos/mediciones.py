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


def medir_tiempo(funcion):
    inicio = time.perf_counter()
    funcion()
    fin = time.perf_counter()

    return fin - inicio


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

        # Búsqueda lineal
        tiempo = medir_tiempo(
            lambda: busqueda_lineal(
                datos,
                "Raichu",
                clave
            )
        )
        print("Busqueda lineal:", tiempo, "segundos")

        # Preparar lista ordenada para búsqueda binaria
        ordenados = ordenar_insercion(datos, clave)

        tiempo = medir_tiempo(
            lambda: busqueda_binaria(
                ordenados,
                "Raichu",
                clave
            )
        )
        print("Busqueda binaria:", tiempo, "segundos")

        # Ordenamiento por selección
        tiempo = medir_tiempo(
            lambda: ordenar_seleccion(datos, clave)
        )
        print("Ordenamiento seleccion:", tiempo, "segundos")

        # Ordenamiento por inserción
        tiempo = medir_tiempo(
            lambda: ordenar_insercion(datos, clave)
        )
        print("Ordenamiento insercion:", tiempo, "segundos")
      
    if __name__ == "__main__":
    ejecutar_mediciones()
