import sqlite3
from src.gestor.usuario import Usuario
from src.gestor.tarea import Tarea
from datetime import datetime
class Gestor:
    def __init__(self) -> None:        
        self.sesion_actual = None   
        self.db_nombre = "docs/gestor.db"
        self._crear_tabla_usuarios()
        self._crear_tabla_tareas()

         
#? Usuarios ----------

    def _crear_tabla_usuarios(self):
        with sqlite3.connect(self.db_nombre) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT UNIQUE NOT NULL,
                    contraseña TEXT NOT NULL
                )
            """)
            conn.commit()

    def registrar_usuario(self, nombre, contraseña):
        try:
            with sqlite3.connect(self.db_nombre) as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO usuarios (nombre, contraseña) VALUES (?, ?)", (nombre, contraseña))
                conn.commit()
            return "Usuario registrado con éxito"
        except sqlite3.IntegrityError:
            return "Este usuario ya existe"

    def iniciar_sesion(self, nombre, contraseña):
        with sqlite3.connect(self.db_nombre) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE nombre = ? AND contraseña = ?", (nombre, contraseña))
            usuario = cursor.fetchone()
            if usuario:
                self.sesion_actual = usuario 
                return f"Bienvenido {nombre}"
            return "Usuario o contraseña incorrectos"
        
    def cerrar_sesion(self):
        self.sesion_actual = None
        return "Sesión cerrada"

#? Tareas ----------

    def _crear_tabla_tareas(self):
        with sqlite3.connect(self.db_nombre) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tareas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    descripcion TEXT NOT NULL,
                    categoria TEXT NOT NULL,
                    fecha_creacion TEXT NOT NULL,
                    fecha_limite TEXT NOT NULL,
                    estado TEXT NOT NULL,
                    usuario_id INTEGER NOT NULL,
                    FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
                )
            """)
            
    def agregar_tarea(self, nombre, descripcion, categoria, fecha_limite):
        if self.sesion_actual is None:
            return "Inicia sesión para agregar tareas"
        fecha_creacion = datetime.now().strftime("%d/%m/%Y %H:%M")
        with sqlite3.connect(self.db_nombre) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO tareas (nombre, descripcion, categoria, fecha_creacion, fecha_limite, estado, usuario_id) VALUES (?, ?, ?, ?, ?, ?, ?)", (nombre, descripcion, categoria,fecha_creacion, fecha_limite, "pendiente", self.sesion_actual[0]))
            conn.commit()
        return "Tarea agregada"
    
    def ver_tareas(self):
        """Muestra solo las tareas del usuario en sesión."""
        if self.sesion_actual is None:
            return "Inicia sesión para ver tareas"
        
        with sqlite3.connect(self.db_nombre) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tareas WHERE usuario_id = ?", (self.sesion_actual[0],))
            tareas = cursor.fetchall()

        if not tareas:
            return "\nNo tienes tareas registradas."

        for i, tarea in enumerate(tareas, start=1):
            print(f"""
TAREA {i}
-------------------
Nombre: {tarea[1]}
Descripción: {tarea[2]}
Categoría: {tarea[3]}
Fecha de Creación: {tarea[4]}
Fecha Límite: {tarea[5]}
Estado: {tarea[6]}
-------------------
""")
    
    def eliminar_tarea(self, nombre):
        if self.sesion_actual is None:
            return "Inicia sesión para eliminar tareas"
        with sqlite3.connect(self.db_nombre) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tareas WHERE nombre = ? AND usuario_id = ?", (nombre, self.sesion_actual[0]))
            conn.commit()
        return "Tarea eliminada"

    