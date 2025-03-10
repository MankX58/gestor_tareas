import unittest
from src.gestor import Gestor

class TestGestor(unittest.TestCase):
    def setUp(self):
        self.gestor = Gestor()
        self.gestor.registrar_usuario("testuser", "password")

    def test_registrar_usuario(self):
        self.assertEqual(self.gestor.registrar_usuario("nuevo", "pass"), "Usuario registrado")
        self.assertEqual(self.gestor.registrar_usuario("testuser", "password"), "Este usuario ya existe")
    
    def test_iniciar_sesion(self):
        self.assertEqual(self.gestor.iniciar_sesion("testuser", "password"), "Bienvenido testuser")
        self.assertEqual(self.gestor.iniciar_sesion("testuser", "wrong"), "Contraseña incorrecta")
        self.assertEqual(self.gestor.iniciar_sesion("nouser", "password"), "Este usuario no existe")
    
    def test_agregar_tarea(self):
        self.gestor.iniciar_sesion("testuser", "password")
        self.assertEqual(self.gestor.agregar_tarea("Hacer ejercicio", "Descripción", "2024-03-10"), "Tarea agregada")
    
    def test_ver_tareas(self):
        self.gestor.iniciar_sesion("testuser", "password")
        self.gestor.agregar_tarea("Estudiar", "Descripción", "2024-03-10")
        tareas = self.gestor.ver_tareas()
        self.assertEqual(len(tareas), 1)
        self.assertIn("Estudiar", tareas[0])
    
    def test_eliminar_tarea(self):
        self.gestor.iniciar_sesion("testuser", "password")
        self.gestor.agregar_tarea("Dormir temprano", "Descripción", "2024-03-10")
        self.assertEqual(self.gestor.eliminar_tarea("Dormir temprano"), "Tarea eliminada")
        self.assertEqual(len(self.gestor.ver_tareas()), 0)
    
    def test_cerrar_sesion(self):
        self.gestor.iniciar_sesion("testuser", "password")
        self.assertEqual(self.gestor.cerrar_sesion(), "Sesión cerrada")
        self.assertEqual(self.gestor.ver_tareas(), "Inicia sesión para ver tareas")

if __name__ == "__main__":
    unittest.main()
