# Informe del TP

Completar y hacer crecer en cada entrega. No hace falta prosa larga: oraciones claras y tablas.

## 1. Grupo y tema

- Tema: Pokedex
- Por qué lo eligieron (5–8 líneas):

  eleji el tema ya que es algo de lo que se bastante mas que los otros y ademas me gusta Pokemon

## 2. Modelo

Qué es un ítem del catálogo. Qué es mutable y qué no (E1). Cómo se relacionan catálogo, colección principal, pila y cola.

Un item del catalago (en mi caso) representaria a un Pokemon con su nombre y tipo, lo q no es mutable son los datos del catalogo y lo q si seria es cambiarlos en la coleccion principal (asi como lo dije me gusta y entiendo al explicarlo), el catalogo y la coleccion principal se relacionarian ya q una contiene los items disponibles (en mi caso Pokemones) y la otra guarda los q se seleccionen, la pila y la cola se relacionan y funcionan a la par ya q ellas nos ayudan a ordenar los pokemon (mi caso) como se necesite para el programa funcione.

(pueden pegar un diagrama ASCII o una lista de clases)
```

## 3. Recursión (E2)

- Función:
  "mostrar_evoluciones(pokemon_actual)"
- Caso base:
  Cuando el pokemon q se elija no tiene evoluciones la función terminaria
- Caso recursivo:
  Por cada evolución del pokemon actual, la función vuelve a llamarse con esa evolucion
- Traza de un ejemplo real del dataset:
  EJ Pichu:
  1. Se llama (o elije) al pokemon (en este caso Pichu)
    "mostrar_evoluciones(Pichu)"
  2. Se muestra "Pichu"
  3. Pichu tiene como evoluciones a Pikachu, entonces se llama a
    "mostrar_evoluciones(Pikachu)"
  4. Se muestra a "Pikachu"
  5. Pikachu tiene como evoluciones a Raichu, entonces se llama a
    "mostrar_evoluciones(Raichu)"
  6. Se muestra a "Raichu"
  7. Como Raichu ya no tiene evoluciones se volveria al caso base x lo q la funcion termina

## 4. TADs (E3)

| TAD | Operaciones | Invariante |
| --- | --- | --- |
| ListaEnlazada |  |  |
| Pila |  |  |
| Cola |  |  |

Dónde se usa cada uno en el dominio.

## 5. Complejidad (E4)

| Operación | Tiempo | Espacio | Por qué |
| --- | --- | --- | --- |
|  |  |  |  |

Mediciones (`time.perf_counter`):

| Operación | n | segundos |
| --- | --- | --- |
|  |  |  |

## 6. Persistencia (E5)

- Layout del registro binario (campos, `struct`, anchos):
- Header:
- Cómo se actualiza un registro por posición:

## 7. Reparto de trabajo (E6)

| Integrante | Qué hizo | Qué puede defender |
| --- | --- | --- |
|  |  |  |
