from src.dominio.pokemon import pokemon 

bulbasaur = pokemon("Bulbasaur" , "Planta")
ivysaur = pokemon("Ivysaur" , "Planta")
venusaur = pokemon("Venusaur" , "Planta")

charmander = pokemon("Charmander" , "Fuego")
charmeleon = pokemon("Charmeleon" , "Fuego")
charizard = pokemon("Charizard" , "Fuego")

squirtle = pokemon("Squirtle" , "Agua")
wartortle = pokemon("Wartortle" , "Agua")
blastoise = pokemon("Blastoise" , "Agua")

pichu = pokemon("Pichu" , "Electrico")
pikachu = pokemon("Pikachu" , "Electrico")
raichu = pokemon("Raichu" , "Electrico")

eevee = pokemon("Eevee" , "Normal")
vaporeon = pokemon("Vaporeon" , "Agua")
jolteon = pokemon("Jolteon" , "Electrico")
flareon = pokemon("Flareon" , "Fuego")

bulbasaur.evoluciones = [ivysaur]
ivysaur.evoluciones = [venusaur]

charmander.evoluciones = [charmeleon]
charmeleon.evoluciones = [charizard]

squirtle.evoluciones = [wartortle]
wartortle.evoluciones = [blastoise]

pichu.evoluciones = [pikachu]
pikachu.evoluciones = [raichu]

eevee.evoluciones = [vaporeon, jolteon, flareon]

catalogo = [
  bulbasaur,
  ivysaur,
  venusaur,
  charmander,
  charmeleon,
  charizard,
  squirtle,
  wartortle,
  blastoise,
  pichu,
  pikachu,
  raichu,
  eevee,
  vaporeon,
  jolteon,
  flareon
]

def listar_catalogo ():
  for pokemon in catalogo:
      print(F"{pokemon.nombre} - {pokemon.tipo}")

def mostrar_evoluciones(pokemon_actual):
  print(pokemon_actual.nombre)

  if not pokemon_actual.evoluciones:
    return

  for evoluciones in pokemon_actual.evoluciones:
    mostrar_evoluciones(evolucion)
