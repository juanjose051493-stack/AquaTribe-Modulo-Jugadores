import sqlite3

def conectar():
    conexion = sqlite3.connect("aqua_tribe.db")
    return conexion

def crear_tabla():
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
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM jugadores")
    jugadores = cursor.fetchall()
    conexion.close()

    if not jugadores:
        print("\nNo hay jugadores registrados.\n")
    else:
        print("\n===== LISTA DE JUGADORES =====")
        for jugador in jugadores:
            print(f"ID: {jugador[0]} | Nombre: {jugador[1]} | Tribu: {jugador[2]} | Vida: {jugador[3]} | Nivel: {jugador[4]}")
        print("==============================\n")
    
    return jugadores

def actualizar_jugador(id_jugador, nombre, tribu, vida, nivel):
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
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM jugadores WHERE id=?", (id_jugador,))
    conexion.commit()
    conexion.close()
    print(f"Jugador con ID {id_jugador} eliminado.")
