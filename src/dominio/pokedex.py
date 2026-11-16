from src.dominio.pokemon import pokemon
from src.tads.lista_enlazada import ListaEnlazada
from src.excepciones import ItemNoEncontradoError


bulbasaur = pokemon("Bulbasaur", "Planta")
ivysaur = pokemon("Ivysaur", "Planta")
venusaur = pokemon("Venusaur", "Planta")

charmander = pokemon("Charmander", "Fuego")
charmeleon = pokemon("Charmeleon", "Fuego")
charizard = pokemon("Charizard", "Fuego")

squirtle = pokemon("Squirtle", "Agua")
wartortle = pokemon("Wartortle", "Agua")
blastoise = pokemon("Blastoise", "Agua")

pichu = pokemon("Pichu", "Electrico")
pikachu = pokemon("Pikachu", "Electrico")
raichu = pokemon("Raichu", "Electrico")

eevee = pokemon("Eevee", "Normal")
vaporeon = pokemon("Vaporeon", "Agua")
jolteon = pokemon("Jolteon", "Electrico")
flareon = pokemon("Flareon", "Fuego")


bulbasaur.evoluciones = [ivysaur]
ivysaur.evoluciones = [venusaur]

charmander.evoluciones = [charmeleon]
charmeleon.evoluciones = [charizard]

squirtle.evoluciones = [wartortle]
wartortle.evoluciones = [blastoise]

pichu.evoluciones = [pikachu]
pikachu.evoluciones = [raichu]

eevee.evoluciones = [vaporeon, jolteon, flareon]


catalogo = ListaEnlazada()

catalogo.insertar_al_final(bulbasaur)
catalogo.insertar_al_final(ivysaur)
catalogo.insertar_al_final(venusaur)

catalogo.insertar_al_final(charmander)
catalogo.insertar_al_final(charmeleon)
catalogo.insertar_al_final(charizard)

catalogo.insertar_al_final(squirtle)
catalogo.insertar_al_final(wartortle)
catalogo.insertar_al_final(blastoise)

catalogo.insertar_al_final(pichu)
catalogo.insertar_al_final(pikachu)
catalogo.insertar_al_final(raichu)

catalogo.insertar_al_final(eevee)
catalogo.insertar_al_final(vaporeon)
catalogo.insertar_al_final(jolteon)
catalogo.insertar_al_final(flareon)


def listar_catalogo():
    for p in catalogo:
        print(f"{p.nombre} - {p.tipo1}")


def buscar_pokemon(nombre):
    for p in catalogo:
        if p.nombre.lower() == nombre.lower():
            return p
    raise ItemNoEncontradoError("No se encontró ese Pokémon.")


def buscar_por_id(id_pokemon):
    for p in catalogo:
        if p.id == int(id_pokemon):
            return p
    raise ItemNoEncontradoError("No se encontró ese ID.")


def mostrar_evoluciones(pokemon_actual):
    print(pokemon_actual.nombre)
    for evolucion in pokemon_actual.evoluciones:
        mostrar_evoluciones(evolucion)


def armar_catalogo_desde_txt(ruta):
    from pathlib import Path
    from src.persistencia.texto import cargar_texto

    nuevo = ListaEnlazada()
    por_id = {}

    for fila in cargar_texto(ruta):
        p = pokemon(
            fila["nombre"],
            fila["tipo1"],
            id=fila["id"],
            tipo2=fila.get("tipo2"),
            hp=fila.get("hp", 0),
            ataque=fila.get("ataque", 0),
            defensa=fila.get("defensa", 0),
            velocidad=fila.get("velocidad", 0),
            generacion=fila.get("generacion", 1)
        )
        nuevo.insertar_al_final(p)
        por_id[p.id] = p

    ruta_evo = Path(ruta).parent / "evoluciones.txt"

    if ruta_evo.exists():
        for fila in cargar_texto(ruta_evo):
            origen = por_id.get(int(fila["origen_id"]))
            destino = por_id.get(int(fila["destino_id"]))

            if origen and destino:
                origen.evoluciones.append(destino)

    return nuevo


def filas_del_catalogo(lista=None):
    lista = catalogo if lista is None else lista

    return [
        {
            "id": p.id,
            "nombre": p.nombre,
            "tipo1": p.tipo1,
            "tipo2": p.tipo2 or "",
            "hp": p.hp,
            "ataque": p.ataque,
            "defensa": p.defensa,
            "velocidad": p.velocidad,
            "generacion": p.generacion
        }
        for p in lista
    ]


def agregar_pokemon(nuevo):
    if any(p.id == nuevo.id for p in catalogo):
        raise ValueError("Ya existe un Pokémon con ese ID.")

    catalogo.insertar_al_final(nuevo)


def eliminar_pokemon(id_pokemon):
    encontrado = buscar_por_id(id_pokemon)
    catalogo.eliminar(encontrado)


def modificar_pokemon(id_pokemon, nombre, tipo1, tipo2,
                      hp, ataque, defensa, velocidad, generacion):
    p = buscar_por_id(id_pokemon)

    p.nombre = nombre
    p.tipo = tipo1
    p.tipo1 = tipo1
    p.tipo2 = tipo2 or None
    p.hp = int(hp)
    p.ataque = int(ataque)
    p.defensa = int(defensa)
    p.velocidad = int(velocidad)
    p.generacion = int(generacion)
