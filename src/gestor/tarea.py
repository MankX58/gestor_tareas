from datetime import datetime

class Tarea:
    def __init__(self, nombre, texto, categoria, fecha_limite = None, usuario = None) -> None:
        self.nombre = nombre
        self.texto = texto
        self.categoria = categoria
        self.usuario = usuario
        self.fecha_creacion = datetime.now().strftime("%d/%m/%Y")
        self.fecha_limite = fecha_limite
        self.estado = 'pendiente'

    def editar(self, nombre = None, texto = None, categoria = None, estado = None) -> None:
        if nombre:
            self.nombre = nombre
        if texto:
            self.texto = texto
        if categoria:
            self.categoria = categoria
        if estado:
            self.estado = estado

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}\nContenido: {self.texto}\nCategoria: {self.categoria}\nFecha de creación: {self.fecha_creacion}\nFecha limite: {self.fecha_limite or 'Sin fecha límite'}"
