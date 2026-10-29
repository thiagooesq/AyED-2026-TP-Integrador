def busqueda_lineal(coleccion, clave, obtener_clave):
    """Devuelve el item cuya clave coincide, o None."""

    for elemento in coleccion:
        if obtener_clave(elemento) == clave:
            return elemento

    return None


def busqueda_binaria(coleccion_ordenada, clave, obtener_clave):
    """Busca un elemento en una colección ordenada."""

    elementos = list(coleccion_ordenada)

    izquierda = 0
    derecha = len(elementos) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        valor = obtener_clave(elementos[medio])

        if valor == clave:
            return elementos[medio]

        elif valor < clave:
            izquierda = medio + 1

        else:
            derecha = medio - 1

    return None
