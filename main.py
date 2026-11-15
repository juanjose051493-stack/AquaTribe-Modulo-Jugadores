# ============================================================
# Módulo: Gestión de Jugadores - Aqua Tribe Survival
# Archivo: main.py
# Descripción: Menú principal del módulo. Permite ejecutar
#              las operaciones CRUD de forma interactiva.
# Autor: Juan José Narváez
# Proyecto: Aqua Tribe Survival - SENA ADSO
# ============================================================

from database import crear_tabla, crear_jugador, listar_jugadores, actualizar_jugador, eliminar_jugador
from jugador import Jugador


def menu():
    """
    Función principal que muestra el menú y controla
    las opciones del módulo de jugadores.
    """
    # Se asegura de que la tabla exista al iniciar
    crear_tabla()

    while True:
        print("\n===== AQUA TRIBE SURVIVAL - MÓDULO JUGADORES =====")
        print("1. Crear jugador")
        print("2. Listar jugadores")
        print("3. Actualizar jugador")
        print("4. Eliminar jugador")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        # Opción 1: Crear un nuevo jugador
        if opcion == "1":
            nombre = input("Nombre del jugador: ")
            tribu = input("Tribu: ")
            vida = int(input("Puntos de vida: "))
            nivel = int(input("Nivel: "))
            crear_jugador(nombre, tribu, vida, nivel)

        # Opción 2: Listar todos los jugadores
        elif opcion == "2":
            jugadores = listar_jugadores()
            if len(jugadores) == 0:
                print("No hay jugadores registrados.")
            else:
                print("\n--- Lista de Jugadores ---")
                for j in jugadores:
                    print(f"ID: {j[0]} | Nombre: {j[1]} | Tribu: {j[2]} | Vida: {j[3]} | Nivel: {j[4]}")

        # Opción 3: Actualizar un jugador existente
        elif opcion == "3":
            id_jugador = int(input("ID del jugador a actualizar: "))
            nombre = input("Nuevo nombre: ")
            tribu = input("Nueva tribu: ")
            vida = int(input("Nueva vida: "))
            nivel = int(input("Nuevo nivel: "))
            actualizar_jugador(id_jugador, nombre, tribu, vida, nivel)

        # Opción 4: Eliminar un jugador
        elif opcion == "4":
            id_jugador = int(input("ID del jugador a eliminar: "))
            eliminar_jugador(id_jugador)

        # Opción 5: Salir del programa
        elif opcion == "5":
            print("Saliendo del módulo... ¡Hasta pronto!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")


# Punto de entrada del programa
if __name__ == "__main__":
    menu()