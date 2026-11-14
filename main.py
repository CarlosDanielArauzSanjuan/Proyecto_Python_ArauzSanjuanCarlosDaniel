import json
from pathlib import Path

from modulos.usuarios import gestionar_usuarios
from modulos.pacientes import gestionar_pacientes
from modulos.diagnosticos import diagnosticar_paciente
from modulos.historia import consultar_historia
from modulos.validaciones import esperar_volver


ruta = Path(__file__).parent / "datos" / "clinica.json"

# LECTURA JSON
try:
    with ruta.open("r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
except FileNotFoundError:
    print("No se encontró el archivo datos/clinica.json.")
    raise SystemExit(1)
except json.JSONDecodeError:
    print("El archivo datos/clinica.json no contiene JSON válido.")
    raise SystemExit(1)

# print(datos["usuarios"][0]["correo"])

print("\n╔══════════════════════════════════════╗")
print("║           ACCESO CLÍNICA ACME        ║")
print("╚══════════════════════════════════════╝")
acceso_concedido = False

while acceso_concedido == False:
    correo_ingresado = input("Correo: ")
    contrasena_ingresada = input("Contraseña: ")
    correo_encontrado = False

    for usuario in datos["usuarios"]:
        if usuario["correo"] == correo_ingresado:
            correo_encontrado = True
            if usuario["contrasena"] == contrasena_ingresada:
                acceso_concedido = True
            else:
                print("Contraseña incorrecta. Intenta de nuevo.")
            break

    if correo_encontrado == False:
        print("Correo no encontrado. Intenta de nuevo.")


# ============================== MENÚ INICIAL ================================

# if acceso_concedido:
#     while:
#         match:
#             case:
#                 acción

if acceso_concedido:
    sesion_activa = True

    while sesion_activa:
        print("\n╔══════════════════════════════════════╗")
        print("║             CLÍNICA ACME             ║")
        print("║            MENÚ PRINCIPAL            ║")
        print("╠══════════════════════════════════════╣")
        print("║ Sesión:", usuario["nombres"], usuario["apellidos"])
        print("╠══════════════════════════════════════╣")
        print("║ 1. Gestionar pacientes               ║")

        if "medico" in usuario["roles"]:
            print("║ 2. Diagnosticar paciente             ║")

        print("║ 3. Historia clínica                  ║")
        print("║ 4. Cerrar sesión                     ║")

        if "administrativo" in usuario["roles"]:
            print("║ 0. Gestionar usuarios                ║")

        print("╚══════════════════════════════════════╝")
        opcion = input("Selecciona una opción: ").strip()

        match opcion:
            case "0":
                if "administrativo" in usuario["roles"]:
                    gestionar_usuarios(datos, ruta, usuario)
                else:
                    print("Opción no disponible.")
                    esperar_volver("1. Volver al menú principal: ")

            case "1":
                gestionar_pacientes(datos, ruta)

            case "2":
                if "medico" in usuario["roles"]:
                    diagnosticar_paciente(datos, usuario, ruta)
                else:
                    print("Opción no disponible.")
                    esperar_volver("1. Volver al menú principal: ")

            case "3":
                consultar_historia(datos)

            case "4":
                sesion_activa = False
                print("Sesión cerrada.")

            case _:
                print("Opción inválida.")
                esperar_volver("1. Volver al menú principal: ")
