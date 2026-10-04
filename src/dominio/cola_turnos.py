from src.tads.cola import Cola


class ColaTurnos:

    def __init__(self):
        self._cola = Cola()

    def agregar_turno(self, pokemon):
        self._cola.encolar(pokemon)

    def siguiente_turno(self):
        return self._cola.desencolar()
