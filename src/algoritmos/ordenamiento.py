def ordenar_seleccion(coleccion, clave):
    """Ordenamiento por selección."""

    elementos = list(coleccion)
    n = len(elementos)

    for i in range(n):
        menor = i

        for j in range(i + 1, n):
            if clave(elementos[j]) < clave(elementos[menor]):
                menor = j

        temporal = elementos[i]
        elementos[i] = elementos[menor]
        elementos[menor] = temporal

    return elementos


def ordenar_insercion(coleccion, clave):
    """Ordenamiento por inserción."""

    elementos = list(coleccion)

    for i in range(1, len(elementos)):
        actual = elementos[i]
        j = i - 1

        while j >= 0 and clave(elementos[j]) > clave(actual):
            elementos[j + 1] = elementos[j]
            j = j - 1

        elementos[j + 1] = actual

    return elementos
