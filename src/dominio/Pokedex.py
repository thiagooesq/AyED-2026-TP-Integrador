from src.dominio.Pokemon import Pokemon 

catalogo = [
  Pokemon ("Bulbasaur" , "Planta")
  Pokemon ("Charmander" , "Fuego")
  Pokemon ("Squirtle" , "Agua")
  Pokemon ("Pikachu" , "Electrico")
  Pokemon ("Eevee" , "Normal")
]

def listar_catalogo ():
  for Pokemon in catalogo:
      print(F"{Pokemon.nombre} - {Pokemon.tipo}")
