# Protocolo de pruebas

Pruebas **manuales**. Cada fila es un caso. Ejecutar sobre el tag que entregan.

Leyenda de resultado: `pasa` / `no pasa` / `no corrido`.

Mínimos: 8 casos escritos en E2; ejecutados en E3; 15 de regresión en E6 (pila, cola, archivos, recursión, búsquedas).

| ID | Entrega | Acción (pasos en el CLI) | Datos | Resultado esperado | Resultado | Notas |
| --- | --- | --- | --- | --- | --- | --- |
| P01 | E1 | Arrancar el programa y listar catálogo | dataset de la cátedra | lista no vacía, sin traceback |  |  |
| P02 | E1 | Elegir un ítem inexistente | id = -1 | mensaje claro, el menú sigue |  |  |
| P03 | E2 | Elegir "Operación recursiva" e ingresar un pokemon con línea evolutiva | Pichu | imprime Pichu, Pikachu y Raichu | Pasa |  |
| P04 | E2 | Elegir "Operación Recursiva" e ingresar un pokemon sin línea evolutiva | Raichu | imprime solo Raichu y termina | Pasa |  |
| P05 | E3 | Agregar a la colección principal | equipo de 6 | el séptimo falla con excepción propia | Pasa |  |
| P06 | E3 | Desapilar historial vacío | pila vacía | excepción propia, menú sigue | Pasa |  |
| P07 | E3 | Desencolar cola vacía | cola vacía | excepción propia, menú sigue | Pasa |  |
| P08 | E3 | Listar colección con el iterador | 2+ Pokemon | el orden coincide con las inserciones | Pasa |  |
| P09 | E4 | Búsqueda lineal de un nombre que existe |  | lo encuentra | Pasa |  |
| P10 | E4 | Búsqueda lineal de un nombre que no existe |  | no encontrado, sin traceback | Pasa |  |
| P11 | E4 | Búsqueda binaria con catálogo desordenado |  | avisa o reordena; no da un falso hit | Pasa |  |
| P12 | E4 | Ordenar por un criterio y después por otro |  | el orden cambia | Pasa |  |
| P13 | E5 | Guardar en TXT, salir y volver a entrar | Catálogo modificado | Los datos se mantienen después de reiniciar el programa | pasa | Se comprobó que el Pokémon agregado sigue apareciendo |
| P14 | E5 | Guardar en binario y modificar por ID | Pokémon existente | Los cambios se mantienen al recargar el archivo binario | pasa | Se modificó el ataque de Pikachu a 90 y se comprobó después de recargar |
| P15 | E5 | Intentar cargar un archivo binario dañado | Archivo binario con bytes sobrantes | Se lanza ArchivoInvalidoError sin mostrar traceback | pasa | Se detectó el error y se mostró un mensaje controlado |
