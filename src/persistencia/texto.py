from pathlib import Path
from src.excepciones import ArchivoInvalidoError

def cargar_texto(ruta):
    ruta = Path(ruta)

    try:
        with ruta.open("r", encoding="utf-8") as archivo:
            encabezado = archivo.readline().strip().split(",")

            if not encabezado or encabezado == [""]:
                raise ArchivoInvalidoError(
                    "El archivo no tiene encabezado."
                )

            filas = []

            for numero, linea in enumerate(archivo, 2):
                if not linea.strip():
                    continue

                valores = linea.rstrip("\n").split(",")

                if len(valores) != len(encabezado):
                    raise ArchivoInvalidoError(
                        f"Línea {numero}: cantidad de campos incorrecta."
                    )

                filas.append(dict(zip(encabezado, valores)))

            return filas

    except (OSError, UnicodeError) as error:
        raise ArchivoInvalidoError(
            f"No se pudo leer el archivo: {error}"
        ) from error

def guardar_texto(ruta, filas, encabezados):
    ruta = Path(ruta)

    try:
        ruta.parent.mkdir(parents=True, exist_ok=True)

        with ruta.open(
            "w", encoding="utf-8", newline=""
        ) as archivo:

            archivo.write(",".join(encabezados) + "\n")

            for fila in filas:
                valores = [
                    str(fila.get(campo, ""))
                    for campo in encabezados
                ]

                archivo.write(",".join(valores) + "\n")

    except OSError as error:
        raise ArchivoInvalidoError(
            f"No se pudo guardar el archivo: {error}"
        ) from error
