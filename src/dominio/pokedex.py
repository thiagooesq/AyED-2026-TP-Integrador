from src.dominio.pokemon import pokemon 

catalogo = [
  pokemon ("Bulbasaur" , "Planta")
  pokemon ("Charmander" , "Fuego")
  pokemon ("Squirtle" , "Agua")
  pokemon ("Pikachu" , "Electrico")
  pokemon ("Eevee" , "Normal")
]

def listar_catalogo ():
  for pokemon in catalogo:
      print(F"{pokemon.nombre} - {pokemon.tipo}")
