import json
from modulos.validaciones import esperar_volver, pedir_texto


def registrar_paciente(datos, ruta):
    print("\n╔══════════════════════════════════════╗")
    print("║            AGREGAR PACIENTE          ║")
    print("╚══════════════════════════════════════╝")

    identificacion = pedir_texto("Número de identificación: ")

    for paciente in datos["pacientes"]:
        if paciente["identificacion"] == identificacion:
            print("Ya existe un paciente con esa identificación.")
            return

    nombres = pedir_texto("Nombres: ")
    apellidos = pedir_texto("Apellidos: ")
    telefono = pedir_texto("Número de teléfono: ")
    correo = pedir_texto("Correo electrónico: ")
    direccion = pedir_texto("Dirección: ")
    genero = pedir_texto("Género: ")
    estado_civil = pedir_texto("Estado civil: ")

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
    identificacion = pedir_texto("Identificación del paciente que deseas modificar: ")

    for paciente in datos["pacientes"]:
        if paciente["identificacion"] == identificacion:
            print("Deja el campo vacío para conservar el dato actual.")
            nombres = input("Nombres [" + paciente["nombres"] + "]: ").strip()
            apellidos = input("Apellidos [" + paciente["apellidos"] + "]: ").strip()
            telefono = input("Teléfono [" + paciente["telefono"] + "]: ").strip()
            correo = input("Correo [" + paciente["correo"] + "]: ").strip()
            direccion = input("Dirección [" + paciente["direccion"] + "]: ").strip()
            genero = input("Género [" + paciente["genero"] + "]: ").strip()
            estado_civil = input("Estado civil [" + paciente["estado_civil"] + "]: ").strip()

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

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            registrar_paciente(datos, ruta)
            esperar_volver("1. Volver al menú de gestión de pacientes: ")
        elif opcion == "2":
            modificar_paciente(datos, ruta)
            esperar_volver("1. Volver al menú de gestión de pacientes: ")
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")
            esperar_volver("1. Volver al menú de gestión de pacientes: ")
