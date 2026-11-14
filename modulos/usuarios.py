import json


def registrar_usuario(datos, ruta):
    print("\n╔══════════════════════════════════════╗")
    print("║            AGREGAR USUARIO           ║")
    print("╚══════════════════════════════════════╝")

    identificacion = input("Número de identificación: ")
    nombres = input("Nombres: ")
    apellidos = input("Apellidos: ")
    telefono = input("Número de teléfono: ")
    correo = input("Correo electrónico corporativo: ")
    direccion = input("Dirección: ")
    contrasena = input("Contraseña: ")
    rol = input("Rol (administrativo/medico): ")

    while rol != "administrativo" and rol != "medico":
        print("Rol no válido. Escribe administrativo o medico.")
        rol = input("Rol (administrativo/medico): ")

    for usuario in datos["usuarios"]:
        if usuario["identificacion"] == identificacion:
            print("Ya existe un usuario con esa identificación.")
            return
        if usuario["correo"] == correo:
            print("Ya existe un usuario con ese correo.")
            return

    nuevo_usuario = {
        "identificacion": identificacion,
        "nombres": nombres,
        "apellidos": apellidos,
        "telefono": telefono,
        "correo": correo,
        "direccion": direccion,
        "contrasena": contrasena,
        "rol": rol
    }

    datos["usuarios"].append(nuevo_usuario)

    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4)

    print("Usuario agregado correctamente.")


def modificar_usuario(datos, ruta):
    identificacion = input("Identificación del usuario que deseas modificar: ")

    for usuario in datos["usuarios"]:
        if usuario["identificacion"] == identificacion:
            print("Deja el campo vacío para conservar el dato actual.")
            nombres = input("Nombres [" + usuario["nombres"] + "]: ")
            apellidos = input("Apellidos [" + usuario["apellidos"] + "]: ")
            telefono = input("Teléfono [" + usuario["telefono"] + "]: ")
            correo = input("Correo [" + usuario["correo"] + "]: ")
            direccion = input("Dirección [" + usuario["direccion"] + "]: ")
            contrasena = input("Contraseña nueva (vacío conserva la actual): ")
            rol = input("Rol (administrativo/medico, vacío conserva el actual): ")

            if correo != "":
                for otro_usuario in datos["usuarios"]:
                    if otro_usuario["identificacion"] != identificacion and otro_usuario["correo"] == correo:
                        print("Ese correo ya pertenece a otro usuario.")
                        return

            if rol != "":
                while rol != "administrativo" and rol != "medico":
                    print("Rol no válido. Escribe administrativo o medico.")
                    rol = input("Rol (administrativo/medico): ")
                usuario["rol"] = rol

            if nombres != "":
                usuario["nombres"] = nombres
            if apellidos != "":
                usuario["apellidos"] = apellidos
            if telefono != "":
                usuario["telefono"] = telefono
            if correo != "":
                usuario["correo"] = correo
            if direccion != "":
                usuario["direccion"] = direccion
            if contrasena != "":
                usuario["contrasena"] = contrasena

            with open(ruta, "w", encoding="utf-8") as archivo:
                json.dump(datos, archivo, indent=4)

            print("Usuario modificado correctamente.")
            return

    print("No se encontró un usuario con esa identificación.")


def eliminar_usuario(datos, ruta, usuario_actual):
    identificacion = input("Identificación del usuario que deseas eliminar: ")

    for usuario in datos["usuarios"]:
        if usuario["identificacion"] == identificacion:
            if identificacion == "0000":
                print("No se puede eliminar el usuario administrador inicial.")
                return

            if identificacion == usuario_actual["identificacion"]:
                print("No puedes eliminar el usuario de la sesión actual.")
                return

            if usuario["rol"] == "administrativo":
                cantidad_administrativos = 0
                for otro_usuario in datos["usuarios"]:
                    if otro_usuario["rol"] == "administrativo":
                        cantidad_administrativos += 1
                if cantidad_administrativos == 1:
                    print("No se puede eliminar el último usuario administrativo.")
                    return

            datos["usuarios"].remove(usuario)

            with open(ruta, "w", encoding="utf-8") as archivo:
                json.dump(datos, archivo, indent=4)

            print("Usuario eliminado correctamente.")
            return

    print("No se encontró un usuario con esa identificación.")


def gestionar_usuarios(datos, ruta, usuario_actual):
    while True:
        print("\n╔══════════════════════════════════════╗")
        print("║           GESTIÓN DE USUARIOS        ║")
        print("╠══════════════════════════════════════╣")
        print("║ 1. Agregar usuario                   ║")
        print("║ 2. Modificar usuario                 ║")
        print("║ 3. Eliminar usuario                  ║")
        print("║ 0. Volver al menú principal          ║")
        print("╚══════════════════════════════════════╝")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            registrar_usuario(datos, ruta)
        elif opcion == "2":
            modificar_usuario(datos, ruta)
        elif opcion == "3":
            eliminar_usuario(datos, ruta, usuario_actual)
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")
