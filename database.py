# ============================================================
# Módulo: Gestión de Jugadores - Aqua Tribe Survival
# Archivo: database.py
# Descripción: Contiene la conexión a la base de datos SQLite
#              y las operaciones CRUD del módulo de jugadores.
# Autor: Juan José Narváez
# Proyecto: Aqua Tribe Survival - SENA ADSO
# ============================================================

import sqlite3


def conectar():
    """
    Establece la conexión con la base de datos SQLite.
    Retorna el objeto de conexión.
    """
    conexion = sqlite3.connect("aqua_tribe.db")
    return conexion


def crear_tabla():
    """
    Crea la tabla 'jugadores' si no existe.
    Campos: id, nombre, tribu, vida, nivel.
    """
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jugadores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            tribu TEXT NOT NULL,
            vida INTEGER NOT NULL,
            nivel INTEGER NOT NULL
        )
    """)
    conexion.commit()
    conexion.close()
    print("Tabla de jugadores creada correctamente.")


def crear_jugador(nombre, tribu, vida, nivel):
    """
    Inserta un nuevo jugador en la base de datos.
    Parámetros:
        nombre (str): Nombre del superviviente
        tribu (str): Nombre de la tribu
        vida (int): Puntos de vida
        nivel (int): Nivel del jugador
    """
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO jugadores (nombre, tribu, vida, nivel) VALUES (?, ?, ?, ?)",
        (nombre, tribu, vida, nivel)
    )
    conexion.commit()
    conexion.close()
    print(f"Jugador {nombre} creado correctamente.")


def listar_jugadores():
    """
    Consulta y retorna todos los jugadores registrados.
    Retorna: lista de tuplas con los datos de cada jugador.
    """
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM jugadores")
    jugadores = cursor.fetchall()
    conexion.close()
    return jugadores


def actualizar_jugador(id_jugador, nombre, tribu, vida, nivel):
    """
    Actualiza los datos de un jugador existente según su ID.
    """
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(
        "UPDATE jugadores SET nombre=?, tribu=?, vida=?, nivel=? WHERE id=?",
        (nombre, tribu, vida, nivel, id_jugador)
    )
    conexion.commit()
    conexion.close()
    print(f"Jugador con ID {id_jugador} actualizado.")


def eliminar_jugador(id_jugador):
    """
    Elimina un jugador de la base de datos según su ID.
    """
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM jugadores WHERE id=?", (id_jugador,))
    conexion.commit()
    conexion.close()
    print(f"Jugador con ID {id_jugador} eliminado.")