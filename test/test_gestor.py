import unittest
import sqlite3
from src.gestor.gestor import Gestor
from src.gestor.usuario import Usuario
from src.gestor.tarea import Tarea

class TestGestor(unittest.TestCase):
    def setUp(self):
        self.gestor = Gestor()
        self.gestor.registrar_usuario("user1", "password1")
        self.gestor.registrar_usuario("user2", "password2")
        
        with sqlite3.connect(self.gestor.db_nombre) as conn:
            cursor = conn.cursor()
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT UNIQUE NOT NULL,
                    contraseña TEXT NOT NULL
                )
            """)
            conn.commit() 
            
            cursor.execute("DELETE FROM usuarios")  
            conn.commit()  

        with sqlite3.connect(self.gestor.db_nombre) as conn:
            cursor = conn.cursor()
            cursor.execute("VACUUM")  

    def test_registrar_usuario(self):
        resultado = self.gestor.registrar_usuario("testuser", "password123")
        self.assertEqual(resultado, "Usuario registrado con éxito") 
    
    def test_registrar_usuario_existente(self):
        self.gestor.registrar_usuario("testuser", "password123")
        resultado = self.gestor.registrar_usuario("testuser", "password123")
        self.assertEqual(resultado, "Este usuario ya existe")

    def test_iniciar_sesion_correcta(self):
        self.gestor.registrar_usuario("testuser", "password123")
        resultado = self.gestor.iniciar_sesion("testuser", "password123")
        self.assertEqual(resultado, "Bienvenido testuser")

    def test_iniciar_sesion_incorrecta(self):
        self.gestor.registrar_usuario("testuser", "password123")
        resultado = self.gestor.iniciar_sesion("testuser", "wrongpassword")
        self.assertEqual(resultado, "Usuario o contraseña incorrectos")

    def test_agregar_tarea_sin_sesion(self):
        resultado = self.gestor.agregar_tarea("Tarea 1", "Descripción", "Trabajo", "20/03/2025")
        self.assertEqual(resultado, "Inicia sesión para agregar tareas")

    def test_agregar_y_ver_tarea(self):
        self.gestor.registrar_usuario("testuser", "password123")
        self.gestor.iniciar_sesion("testuser", "password123")
        self.gestor.agregar_tarea("Tarea 1", "Descripción", "Trabajo", "20/03/2025")
        with sqlite3.connect(self.gestor.db_nombre) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tareas WHERE usuario_id = ?", (self.gestor.sesion_actual[0],))
            tarea = cursor.fetchone()
            self.assertIsNotNone(tarea)
            self.assertEqual(tarea[1], "Tarea 1")

    def test_eliminar_tarea(self):
        self.gestor.registrar_usuario("testuser", "password123")
        self.gestor.iniciar_sesion("testuser", "password123")
        self.gestor.agregar_tarea("Tarea 1", "Descripción", "Trabajo", "20/03/2025")
        self.gestor.eliminar_tarea("Tarea 1")

        with sqlite3.connect(self.gestor.db_nombre) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tareas WHERE nombre = ? AND usuario_id = ?", 
                           ("Tarea 1", self.gestor.sesion_actual[0]))
            tarea = cursor.fetchone() 

        self.assertIsNone(tarea) 
        
if __name__ == "__main__":
    unittest.main()
