from src.tads.pila import Pila


class Historial:

    def __init__(self):
        self._pila = Pila()

    def visitar(self, pokemon):
        self._pila.apilar(pokemon)

    def deshacer(self):
        return self._pila.desapilar()
