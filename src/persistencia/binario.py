import struct
from pathlib import Path

from src.excepciones import ArchivoInvalidoError
from src.tads.lista_enlazada import ListaEnlazada
from src.dominio.pokemon import pokemon as Pokemon

HEADER = struct.Struct("<4s1sI")
FORMATO = struct.Struct("<I20s12s12s4H")

TEMA = b"P"

def _a_bytes(texto, ancho):
    datos = str(texto or "").encode("utf-8")

    if len(datos) > ancho:
        raise ValueError(
            f"El texto {texto!r} supera {ancho} bytes."
        )

    return datos.ljust(ancho, b"\x00")

def _a_texto(datos):
    return datos.rstrip(b"\x00").decode("utf-8")

def _item_a_tupla(p):
    return (
        int(p.id),
        _a_bytes(p.nombre, 20),
        _a_bytes(p.tipo1, 12),
        _a_bytes(p.tipo2 or "", 12),
        int(p.hp),
        int(p.ataque),
        int(p.defensa),
        int(p.velocidad)
    )

def _tupla_a_item(t):
    return Pokemon(
        _a_texto(t[1]),
        _a_texto(t[2]),
        id=t[0],
        tipo2=_a_texto(t[3]),
        hp=t[4],
        ataque=t[5],
        defensa=t[6],
        velocidad=t[7]
    )

def guardar_binario(ruta, items):
    items = list(items)

    ruta = Path(ruta)
    ruta.parent.mkdir(parents=True, exist_ok=True)

    try:
        with ruta.open("wb") as archivo:
            archivo.write(
                HEADER.pack(b"AYED", TEMA, len(items))
            )

            for item in items:
                archivo.write(
                    FORMATO.pack(*_item_a_tupla(item))
                )

    except (OSError, ValueError, struct.error) as error:
        raise ArchivoInvalidoError(
            f"No se pudo guardar el binario: {error}"
        ) from error

def cargar_binario(ruta):
    try:
        with Path(ruta).open("rb") as archivo:
            cabecera = archivo.read(HEADER.size)

            if len(cabecera) != HEADER.size:
                raise ArchivoInvalidoError(
                    "Header incompleto."
                )

            magia, tema, cantidad = HEADER.unpack(cabecera)

            if magia != b"AYED":
                raise ArchivoInvalidoError(
                    "Magia incorrecta."
                )

            if tema != TEMA:
                raise ArchivoInvalidoError(
                    "El tema no corresponde a Pokédex."
                )

            catalogo = ListaEnlazada()

            for _ in range(cantidad):
                datos = archivo.read(FORMATO.size)

                if len(datos) != FORMATO.size:
                    raise ArchivoInvalidoError(
                        "Binario truncado: faltan registros."
                    )

                item = _tupla_a_item(
                    FORMATO.unpack(datos)
                )

                catalogo.insertar_al_final(item)

            if archivo.read(1):
                raise ArchivoInvalidoError(
                    "El archivo contiene bytes sobrantes."
                )

            return catalogo

    except ArchivoInvalidoError:
        raise

    except (OSError, UnicodeError, struct.error) as error:
        raise ArchivoInvalidoError(
            f"No se pudo leer el binario: {error}"
        ) from error

def actualizar_registro(ruta, posicion, item):
    if posicion < 0:
        raise IndexError(
            "La posición no puede ser negativa."
        )

    try:
        with Path(ruta).open("r+b") as archivo:
            cabecera = archivo.read(HEADER.size)

            if len(cabecera) != HEADER.size:
                raise ArchivoInvalidoError(
                    "Header incompleto."
                )

            magia, tema, cantidad = HEADER.unpack(cabecera)

            if magia != b"AYED" or tema != TEMA:
                raise ArchivoInvalidoError(
                    "Header o tema inválido."
                )

            if posicion >= cantidad:
                raise IndexError(
                    "Posición fuera del catálogo."
                )

            archivo.seek(
                HEADER.size + posicion * FORMATO.size
            )

            archivo.write(
                FORMATO.pack(*_item_a_tupla(item))
            )

    except ArchivoInvalidoError:
        raise

    except (OSError, struct.error, ValueError) as error:
        raise ArchivoInvalidoError(
            f"No se pudo actualizar el registro: {error}"
        ) from error
