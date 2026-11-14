import json
from modulos.validaciones import esperar_volver, pedir_rol, pedir_texto


def registrar_usuario(datos, ruta):
    print("\n╔══════════════════════════════════════╗")
    print("║            AGREGAR USUARIO           ║")
    print("╚══════════════════════════════════════╝")

    identificacion = pedir_texto("Número de identificación: ")
    nombres = pedir_texto("Nombres: ")
    apellidos = pedir_texto("Apellidos: ")
    telefono = pedir_texto("Número de teléfono: ")
    correo = pedir_texto("Correo electrónico corporativo: ")
    direccion = pedir_texto("Dirección: ")
    contrasena = pedir_texto("Contraseña: ")
    rol = pedir_rol("Rol (administrativo/medico/ambos): ")

    if rol == "ambos":
        roles = ["administrativo", "medico"]
    else:
        roles = [rol]

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
        "roles": roles
    }

    datos["usuarios"].append(nuevo_usuario)

    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4)

    print("Usuario agregado correctamente.")


def modificar_usuario(datos, ruta):
    identificacion = pedir_texto("Identificación del usuario que deseas modificar: ")

    for usuario in datos["usuarios"]:
        if usuario["identificacion"] == identificacion:
            print("Deja el campo vacío para conservar el dato actual.")
            nombres = input("Nombres [" + usuario["nombres"] + "]: ").strip()
            apellidos = input("Apellidos [" + usuario["apellidos"] + "]: ").strip()
            telefono = input("Teléfono [" + usuario["telefono"] + "]: ").strip()
            correo = input("Correo [" + usuario["correo"] + "]: ").strip()
            direccion = input("Dirección [" + usuario["direccion"] + "]: ").strip()
            contrasena = input("Contraseña nueva (vacío conserva la actual): ").strip()
            roles_actuales = " / ".join(usuario["roles"])
            rol = pedir_rol("Rol (administrativo/medico/ambos, vacío conserva " + roles_actuales + "): ", permitir_vacio=True)

            if correo != "":
                for otro_usuario in datos["usuarios"]:
                    if otro_usuario["identificacion"] != identificacion and otro_usuario["correo"] == correo:
                        print("Ese correo ya pertenece a otro usuario.")
                        return

            if rol != "":
                if rol == "ambos":
                    roles_nuevos = ["administrativo", "medico"]
                else:
                    roles_nuevos = [rol]

                if "administrativo" in usuario["roles"] and "administrativo" not in roles_nuevos:
                    cantidad_administrativos = 0
                    for otro_usuario in datos["usuarios"]:
                        if "administrativo" in otro_usuario["roles"]:
                            cantidad_administrativos += 1
                    if cantidad_administrativos == 1:
                        print("No se puede cambiar el rol del último usuario administrativo.")
                        return

                usuario["roles"] = roles_nuevos

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
    identificacion = pedir_texto("Identificación del usuario que deseas eliminar: ")

    for usuario in datos["usuarios"]:
        if usuario["identificacion"] == identificacion:
            if identificacion == "0000":
                print("No se puede eliminar el usuario administrador inicial.")
                return

            if identificacion == usuario_actual["identificacion"]:
                print("No puedes eliminar el usuario de la sesión actual.")
                return

            if "administrativo" in usuario["roles"]:
                cantidad_administrativos = 0
                for otro_usuario in datos["usuarios"]:
                    if "administrativo" in otro_usuario["roles"]:
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

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            registrar_usuario(datos, ruta)
            esperar_volver("1. Volver al menú de gestión de usuarios: ")
        elif opcion == "2":
            modificar_usuario(datos, ruta)
            esperar_volver("1. Volver al menú de gestión de usuarios: ")
        elif opcion == "3":
            eliminar_usuario(datos, ruta, usuario_actual)
            esperar_volver("1. Volver al menú de gestión de usuarios: ")
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")
            esperar_volver("1. Volver al menú de gestión de usuarios: ")
