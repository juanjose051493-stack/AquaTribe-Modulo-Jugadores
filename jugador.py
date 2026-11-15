# ============================================================
# Módulo: Gestión de Jugadores - Aqua Tribe Survival
# Archivo: jugador.py
# Descripción: Define la clase Jugador (modelo del superviviente).
# Autor: Juan José Narváez
# Proyecto: Aqua Tribe Survival - SENA ADSO
# ============================================================

class Jugador:
    """
    Clase que representa a un jugador / superviviente
    del videojuego Aqua Tribe Survival.
    """

    def __init__(self, nombre, tribu, vida, nivel):
        """
        Constructor de la clase Jugador.
        Inicializa los atributos del superviviente.
        """
        self.nombre = nombre      # Nombre del jugador
        self.tribu = tribu        # Tribu a la que pertenece
        self.vida = vida          # Puntos de vida actuales
        self.nivel = nivel        # Nivel de experiencia

    def mostrar_info(self):
        """
        Muestra en pantalla la información del jugador.
        """
        print(f"Nombre: {self.nombre}")
        print(f"Tribu: {self.tribu}")
        print(f"Vida: {self.vida}")
        print(f"Nivel: {self.nivel}")
        print("-" * 30)