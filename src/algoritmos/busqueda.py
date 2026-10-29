def busqueda_lineal(coleccion, clave, obtener_clave):
    """Devuelve el item cuya clave coincide, o None."""

    for elemento in coleccion:
        if obtener_clave(elemento) == clave:
            return elemento

    return None

def busqueda_binaria(coleccion_ordenada, clave, obtener_clave):
    """Busca un elemento en una colección ordenada."""

    izquierda = 0
    derecha = len(coleccion_ordenada) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        valor = obtener_clave(coleccion_ordenada[medio])

        if valor == clave:
            return coleccion_ordenada[medio]

        elif valor < clave:
            izquierda = medio + 1

        else:
            derecha = medio - 1

    return None
