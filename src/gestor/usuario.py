class Usuario:
    def __init__(self, nombre, contraseña) -> None:
        self.nombre = nombre
        self.contraseña = contraseña
        self.tareas = []

    def cambiar_contraseña(self, nueva_contraseña) -> None:
        self.contraseña = nueva_contraseña

    def verificar_contraseña(self, contraseña) -> bool:
        return self.contraseña == contraseña
    
    def agregar_tarea(self, tarea) -> None:
        self.tareas.append(tarea)
        
    def ver_tareas(self) -> list:
        for i, tarea in enumerate(self.tareas, start=1):
            print(f"\nTAREA {i}\n-------------------\n{tarea}\n-------------------")
        
    def eliminar_tarea(self, nombre) -> None:
        self.tareas = [tarea for tarea in self.tareas if tarea.nombre != nombre]