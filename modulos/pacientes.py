import json


def registrar_paciente(datos, ruta):
    print("\n╔══════════════════════════════════════╗")
    print("║            AGREGAR PACIENTE          ║")
    print("╚══════════════════════════════════════╝")

    identificacion = input("Número de identificación: ")

    for paciente in datos["pacientes"]:
        if paciente["identificacion"] == identificacion:
            print("Ya existe un paciente con esa identificación.")
            return

    nombres = input("Nombres: ")
    apellidos = input("Apellidos: ")
    telefono = input("Número de teléfono: ")
    correo = input("Correo electrónico: ")
    direccion = input("Dirección: ")
    genero = input("Género: ")
    estado_civil = input("Estado civil: ")

    nuevo_paciente = {
        "identificacion": identificacion,
        "nombres": nombres,
        "apellidos": apellidos,
        "telefono": telefono,
        "correo": correo,
        "direccion": direccion,
        "genero": genero,
        "estado_civil": estado_civil
    }

    datos["pacientes"].append(nuevo_paciente)

    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4)

    print("Paciente agregado correctamente.")


def modificar_paciente(datos, ruta):
    identificacion = input("Identificación del paciente que deseas modificar: ")

    for paciente in datos["pacientes"]:
        if paciente["identificacion"] == identificacion:
            print("Deja el campo vacío para conservar el dato actual.")
            nombres = input("Nombres [" + paciente["nombres"] + "]: ")
            apellidos = input("Apellidos [" + paciente["apellidos"] + "]: ")
            telefono = input("Teléfono [" + paciente["telefono"] + "]: ")
            correo = input("Correo [" + paciente["correo"] + "]: ")
            direccion = input("Dirección [" + paciente["direccion"] + "]: ")
            genero = input("Género [" + paciente["genero"] + "]: ")
            estado_civil = input("Estado civil [" + paciente["estado_civil"] + "]: ")

            if nombres != "":
                paciente["nombres"] = nombres
            if apellidos != "":
                paciente["apellidos"] = apellidos
            if telefono != "":
                paciente["telefono"] = telefono
            if correo != "":
                paciente["correo"] = correo
            if direccion != "":
                paciente["direccion"] = direccion
            if genero != "":
                paciente["genero"] = genero
            if estado_civil != "":
                paciente["estado_civil"] = estado_civil

            with open(ruta, "w", encoding="utf-8") as archivo:
                json.dump(datos, archivo, indent=4)

            print("Paciente modificado correctamente. La identificación se conserva para mantener sus consultas asociadas.")
            return

    print("No se encontró un paciente con esa identificación.")


def gestionar_pacientes(datos, ruta):
    while True:
        print("\n╔══════════════════════════════════════╗")
        print("║           GESTIÓN DE PACIENTES       ║")
        print("╠══════════════════════════════════════╣")
        print("║ 1. Agregar paciente                  ║")
        print("║ 2. Modificar paciente                ║")
        print("║ 0. Volver al menú principal          ║")
        print("╚══════════════════════════════════════╝")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            registrar_paciente(datos, ruta)
        elif opcion == "2":
            modificar_paciente(datos, ruta)
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")
