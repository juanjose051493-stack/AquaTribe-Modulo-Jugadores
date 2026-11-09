# Módulo de Gestión de Jugadores

### 1. Información de la evidencia

**Código:** GA7-220501096-AA2-EV01  
**Nombre:** Codificación de Módulos del Software según requerimientos del proyecto.

### 2. Descripción del módulo

El módulo de Gestión de Jugadores permite administrar la información de los supervivientes del videojuego Aqua Tribe Survival.

El sistema utiliza una base de datos SQLite para almacenar los registros y permite realizar las operaciones CRUD (Crear, Leer, Actualizar y Eliminar).

### 3. Funcionalidades

- **Crear:** registrar nuevos jugadores con nombre, tribu, puntos de vida y nivel.
- **Leer:** consultar y visualizar todos los jugadores registrados.
- **Actualizar:** modificar la información de un jugador existente.
- **Eliminar:** borrar un jugador de la base de datos.

### 4. Tecnologías utilizadas

- Python 3.
- SQLite3.
- Visual Studio Code.
- Git y GitHub.

### 5. Estructura del proyecto

```text
AquaTribe_Modulo_Jugadores/
│
├── main.py
├── jugador.py
├── database.py
├── aqua_tribe.db
└── README.md
```

**Descripción de los archivos:**

- `main.py`: contiene el menú principal y permite interactuar con el usuario.
- `jugador.py`: contiene la clase Jugador y sus atributos.
- `database.py`: administra la conexión con SQLite y las operaciones CRUD.
- `aqua_tribe.db`: almacena la información de los jugadores.
- `README.md`: contiene la documentación del proyecto.

### 6. Estándares de codificación aplicados

Durante el desarrollo se aplicaron los siguientes estándares:

- Uso de nombres de variables y funciones en minúsculas separados por guion bajo (snake_case).
- Uso de nombres de clases con formato PascalCase.
- Implementación de funciones con nombres descriptivos.
- Organización del código en diferentes archivos según sus responsabilidades.
- Uso de consultas SQL parametrizadas para las operaciones con la base de datos.
- Identación y organización del código para facilitar su lectura y mantenimiento.

### 7. Base de datos

Se utilizó SQLite para almacenar los jugadores.

La tabla principal se denomina `jugadores` y contiene los siguientes campos:

| Campo | Tipo de dato | Descripción |
|---|---|---|
| id | INTEGER | Identificador único |
| nombre | TEXT | Nombre del jugador |
| tribu | TEXT | Tribu a la que pertenece |
| vida | INTEGER | Puntos de vida |
| nivel | INTEGER | Nivel del jugador |

### 8. Instalación y ejecución

1. Abrir la carpeta del proyecto en Visual Studio Code.
2. Verificar que Python esté instalado.
3. Abrir la terminal integrada.
4. Ejecutar el siguiente comando:

```bash
python main.py
```

5. Seleccionar la operación deseada en el menú principal.

### 9. Pruebas de funcionamiento

Se realizaron pruebas para comprobar las cuatro operaciones CRUD:

- Creación de jugadores.
- Consulta de jugadores registrados.
- Actualización de los datos de un jugador.
- Eliminación de jugadores.

Las pruebas permitieron comprobar el funcionamiento de las operaciones y la conexión con la base de datos SQLite.

### 10. Conclusión

El desarrollo del módulo de Gestión de Jugadores permitió aplicar conocimientos de programación en Python, conexión con bases de datos SQLite y manejo de operaciones CRUD.

Se obtuvo un módulo funcional que permite administrar la información de los supervivientes de Aqua Tribe Survival, manteniendo una estructura organizada y aplicando buenas prácticas de codificación.

Este módulo constituye una base para futuras funcionalidades del videojuego.