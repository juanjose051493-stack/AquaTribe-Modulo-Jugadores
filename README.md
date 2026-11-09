# Aqua Tribe Survival - Módulo de Gestión de Jugadores

## Evidencia
**GA7-220501096-AA2-EV01**  
Codificación de Módulos del Software según requerimientos del proyecto

## Descripción del módulo
Este módulo permite gestionar los jugadores (supervivientes) del videojuego **Aqua Tribe Survival**.

Incluye las operaciones CRUD:
- **Crear** un nuevo jugador
- **Consultar** (listar) todos los jugadores
- **Actualizar** los datos de un jugador
- **Eliminar** un jugador

## Tecnologías utilizadas
- Python 3
- SQLite3 (base de datos)
- Visual Studio Code

## Estructura del proyecto
- `main.py` → Menú principal del módulo
- `database.py` → Conexión a la base de datos y operaciones CRUD
- `jugador.py` → Clase Jugador
- `aqua_tribe.db` → Base de datos SQLite

## Estándares de codificación aplicados
- Nombres de variables y funciones en minúsculas con guion bajo (snake_case)
- Nombres de clases con la primera letra en mayúscula (PascalCase)
- Funciones con nombres claros y descriptivos
- Código organizado por responsabilidad (separación de archivos)

## Cómo ejecutar
1. Abrir la carpeta en Visual Studio Code
2. Ejecutar en la terminal: