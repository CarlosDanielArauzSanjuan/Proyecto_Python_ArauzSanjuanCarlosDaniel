import json
from pathlib import Path
 
ruta = ruta = Path("datos") / "clinica.json"

with ruta.open("r", encoding="utf-8") as archivo:
    datos = json.load(archivo)

# print(datos["usuarios"][0]["correo"])

print("======= Clínica ACME =======")
correo_ingresado = input("Correo: ")
contrasena_ingresada = input("Contraseña: ")

for usuario in datos["usuarios"]:
    if usuario["correo"] == correo_ingresado:
        if usuario["contrasena"] == contrasena_ingresada:
            print("Acceso concedido")
        else:
            print("Contraseña incorrecta")
        break
else:
    print("Correo no encontrado")
