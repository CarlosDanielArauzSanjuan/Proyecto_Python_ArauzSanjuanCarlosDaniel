import json


def registrar_paciente(datos, ruta):
    identificacion = input("Número de identificación: ")
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
        
        