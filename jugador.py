class Jugador:
    def __init__(self, nombre, tribu, vida, nivel):
        self.nombre = nombre
        self.tribu = tribu
        self.vida = vida
        self.nivel = nivel

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Tribu: {self.tribu}")
        print(f"Vida: {self.vida}")
        print(f"Nivel: {self.nivel}")
        print("-" * 30)