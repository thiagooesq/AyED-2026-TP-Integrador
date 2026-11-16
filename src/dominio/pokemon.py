class pokemon:
    def __init__(
        self, nombre, tipo, id=0, tipo2=None,
        hp=0, ataque=0, defensa=0,
        velocidad=0, generacion=1
    ):
        self.id = int(id)
        self.nombre = nombre
        self.tipo = tipo
        self.tipo1 = tipo
        self.tipo2 = tipo2 or None
        self.hp = int(hp)
        self.ataque = int(ataque)
        self.defensa = int(defensa)
        self.velocidad = int(velocidad)
        self.generacion = int(generacion)
        self.evoluciones = []
