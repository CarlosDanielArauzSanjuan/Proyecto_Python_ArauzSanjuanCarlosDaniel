import json
from pathlib import Path

from modulos.usuarios import registrar_usuario
from modulos.pacientes import registrar_paciente
from modulos.diagnosticos import diagnosticar_paciente
from modulos.historia import consultar_historia


ruta = Path("datos") / "clinica.json"

# LECTURA JSON
with ruta.open("r", encoding="utf-8") as archivo:
    datos = json.load(archivo)

# print(datos["usuarios"][0]["correo"])

print("======= Clínica ACME =======")
correo_ingresado = input("Correo: ")
contrasena_ingresada = input("Contraseña: ")

acceso_concedido = False

for usuario in datos["usuarios"]:
    if usuario["correo"] == correo_ingresado:
        if usuario["contrasena"] == contrasena_ingresada:
            acceso_concedido = True
            break
        else:
            print("Contraseña incorrecta")
            break
else:
    print("Correo no encontrado")


# ============================== MENÚ INICIAL ================================

# if acceso_concedido:
#     while:
#         match:
#             case:
#                 acción

if acceso_concedido:
    sesion_activa = True

    while sesion_activa:
        print("1. Registrar pacientes")
        
        if usuario["rol"] == "medico":
            print("2. Diagnosticar pacientes")
            
        print("3. Consultar historia clínica")
        print("4. Cerrar sesión")

        if usuario["rol"] == "administrativo":
            print("0. Registrar usuarios")

        opcion = input("Elige una opción: ")

        match opcion:
            case "0":
                if usuario["rol"] == "administrativo":
                    registrar_usuario(datos, ruta)
                else:
                    print("Opción no disponible")

            case "1":
                registrar_paciente(datos, ruta)

            case "2":
                if usuario["rol"] == "medico":
                    diagnosticar_paciente(datos, usuario, ruta)
                else:
                    print("Opción no disponible")

            case "3":
                consultar_historia(datos)

            case "4":
                sesion_activa = False

            case _:
                print("Opción inválida")