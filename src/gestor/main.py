from src.gestor.gestor import Gestor

gestor = Gestor()

def menu():
    while True:
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Cerrar sesión")
        print("4. Agregar tarea")
        print("5. Ver tareas")
        print("6. Eliminar tarea")
        print("7, Editar tarea")
        print("8. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            contraseña = input("Contraseña: ")
            print(gestor.registrar_usuario(nombre, contraseña))
            print(gestor.iniciar_sesion(nombre, contraseña))
        elif opcion == "2":
            nombre = input("Nombre: ")
            contraseña = input("Contraseña: ")
            print(gestor.iniciar_sesion(nombre, contraseña))
        elif opcion == "3":
            print(gestor.cerrar_sesion())
        elif opcion == "4":
            nombre = input("Nombre: ")
            descripcion = input("Descripción: ")
            categoria = input("Categoría: ")
            fecha_limite = (input("Fecha límite (dd/mm/yyyy): "))
            print(gestor.agregar_tarea(nombre, descripcion, categoria, fecha_limite))
        elif opcion == "5":
            print(gestor.ver_tareas())
        elif opcion == "6":
            nombre = input("Nombre: ")
            print(gestor.eliminar_tarea(nombre))
        elif opcion == "7":
            nombre = input("Nombre: ")
            descripcion = input("Descripción: ")
            categoria = input("Categoría: ")
            estado = input("Estado: ")
            print(gestor.editar_tarea(nombre, descripcion, categoria, estado))
        elif opcion == "8":
            exit()
        else:
            print("Opción inválida")
            
if __name__ == "__main__":
    print("\n",menu())

