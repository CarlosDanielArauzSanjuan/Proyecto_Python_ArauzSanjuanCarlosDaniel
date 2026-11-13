import json
        
def registrar_usuario(datos, ruta):
    
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
    