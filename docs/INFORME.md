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
| ListaEnlazada | esta_vacia, tamanio, insertar_al_inicio, insertar_al_final, buscar, eliminar, recorrer | Cada nodo apunta al siguiente y la cabeza al primero |
| Pila | apilar, desapilar, ver_tope, esta_vacia | Los elementos se agregan y se sacan por la cabeza, LIFO |
| Cola | encolar, desencolar, ver_frente, esta_vacia | Los elementos entran por el final y salen por la cabeza, FIFO |

Dónde se usa cada uno en el dominio.

RTA: En el dominio, la "ListaEnlazada" se usa para el catalogo y el equipo Pokemon, la "Pila" se usa para el historial de Pokemones visitados y la "Cola" se usa para los turnos en el combate

## 5. Complejidad (E4)

| Operación | Tiempo | Espacio | Por qué |
| --- | --- | --- | --- |
| Listar Catalogo | 0(n) | 0(1) | Recorre todos los pokemon |
| Búsqueda Lineal | 0(n) | 0(1) | Puede recorrer toda la coleccion |
| Búsqueda Binaria | 0(log n) | 0(1) | Divide el intervalo de búsqueda a la mitad |
| Ordenamiento x seleccion | 0(n^2) | 0(n) | Compara elementos y crea una copia |
| Ordenamiento x insercion | 0(n^2) (peor caso, 0(n) mejor caso) | 0(n) | Desplaza elementos y crea una copia |
| Insertar al inicio de lista | 0(1) | 0(1) | Agrega un nodo como cabeza |
| Insertar al final de lista | 0(n) | 0(1) | Recorre la lista hasta el ultimo nodo |
| Buscar o eliminar lista | 0(n) | 0(1) | Puede recorrer todos los nodos |
| Listar Equipo | 0(n) | 0(1) | Recorre el equipo |
| Agregar pokemon al equipo | 0(n) | 0(1) | Inserta al final |
| Apilar | 0(1) | 0(1) | Inserta al inicio |
| Desapilar | 0(1) | 0(1) | Elimina la cabeza |
| Encolar | 0(n) | 0(1) | Inserta al final |
| Desencolar | 0(1) | 0(1) | Elimina la cabeza |

Mediciones (`time.perf_counter`):

| Operación | n | segundos |
| --- | --- | --- |
| Búsqueda lineal |	16 | 0.0000035593 |
| Búsqueda binaria | 16 | 0.0000031862 |
| Selección | 16 | 0.0000676539 |
| Inserción | 16 | 0.0000393539 |
| Búsqueda lineal | 160 | 0.0000265771 |
| Búsqueda binaria | 160 | 0.0000052907 |
| Selección | 160 | 0.0055671 |
| Inserción | 160 | 0.0033721 |
| Búsqueda lineal | 800 | 0.0001275772 |
| Búsqueda binaria | 800 | 0.0000088712 |
| Selección | 800 | 0.1613084 |
| Inserción | 800 | 0.0985432 |

## 6. Persistencia (E5)

- Layout del registro binario (campos, `struct`, anchos):
- Header:
- Cómo se actualiza un registro por posición:

## 7. Reparto de trabajo (E6)

| Integrante | Qué hizo | Qué puede defender |
| --- | --- | --- |
|  |  |  |
