from src.gestor.usuario import Usuario
from src.gestor.tarea import Tarea

class Gestor:
    def __init__(self) -> None:
        self.usuarios = {}
        self.sesion_actual = None   
         
#? Usuarios ----------

    def registrar_usuario(self, nombre, contraseña) -> str:
        if nombre in self.usuarios:
            return "Este usuario ya existe"
        self.usuarios[nombre] = Usuario(nombre, contraseña)
        print("Usuario registrado")
    
    def iniciar_sesion(self, nombre, contraseña) -> str:
        usuario = self.usuarios.get(nombre) 
        if usuario is None:
            return "Este usuario no existe"
        
        if usuario.verificar_contraseña(contraseña):
            self.sesion_actual = usuario
            return f"Bienvenido {nombre}"
        
        return "Contraseña incorrecta"
    
    def cerrar_sesion(self) -> str:
        self.sesion_actual = None
        print("Sesión cerrada")

#? Tareas ----------

    def agregar_tarea(self, nombre, descripcion, categoria, fecha_limite) -> str:
        if self.sesion_actual is None:
            return "Inicia sesión para agregar tareas"
        self.sesion_actual.agregar_tarea(Tarea(nombre, descripcion, categoria, fecha_limite, self.sesion_actual))
        return "Tarea agregada"
    
    def ver_tareas(self) -> str:
        if self.sesion_actual is None:
            return "Inicia sesión para ver tareas"
        print(self.sesion_actual.ver_tareas())
    
    def eliminar_tarea(self, nombre) -> str:
        if self.sesion_actual is None:
            return "Inicia sesión para eliminar tareas"
        self.sesion_actual.eliminar_tarea(nombre)
        return "Tarea eliminada"
    
    