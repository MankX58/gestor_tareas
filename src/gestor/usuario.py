class Usuario:
    def __init__(self, nombre, contraseña) -> None:
        self.nombre = nombre
        self.contraseña = contraseña

    def cambiar_contraseña(self, nueva_contraseña) -> None:
        self.contraseña = nueva_contraseña

    def verificar_contraseña(self, contraseña) -> bool:
        return self.contraseña == contraseña
    