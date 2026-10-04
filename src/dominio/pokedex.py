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
        print(f"{p.nombre} - {p.tipo}")


def buscar_pokemon(nombre):
    for p in catalogo:
        if p.nombre == nombre:
            return p

    raise ItemNoEncontradoError("No se encontró ese Pokémon.")


def mostrar_evoluciones(pokemon_actual):
    print(pokemon_actual.nombre)

    if not pokemon_actual.evoluciones:
        return

    for evolucion in pokemon_actual.evoluciones:
        mostrar_evoluciones(evolucion)
