from src.dominio.pokemon import pokemon 

catalogo = [
  pokemon ("Bulbasaur" , "Planta"),
  pokemon ("Ivysaur" , "Planta"),
  pokemon ("Venusaur" , "Planta"),
  pokemon ("Charmander" , "Fuego"),
  pokemon ("Charmeleon" , "Fuego"),
  pokemon ("Charizard" , "Fuego"),
  pokemon ("Squirtle" , "Agua"),
  pokemon ("Wartortle" , "Agua"),
  pokemon ("Blastoise" , "Agua"),
  pokemon ("Pichu" , "Electrico"),
  pokemon ("Pikachu" , "Electrico"),
  pokemon ("Raichu" , "Electrico"),
  pokemon ("Eevee" , "Normal"),
  pokemon ("Vaporeon" , "Agua"),
  pokemon ("Jolteon" , "Electrico"),
  pokemon ("Flareon" , "Fuego"),
]

def listar_catalogo ():
  for pokemon in catalogo:
      print(F"{pokemon.nombre} - {pokemon.tipo}")
