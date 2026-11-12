import json
from pathlib import Path
 
ruta = ruta = Path("datos") / "clinica.json"

with ruta.open("r", encoding="utf-8") as archivo:
    datos = json.load(archivo)

# print(datos["usuarios"][0]["correo"])

print("======= Clínica ACME =======")
correo_ingresado = input(" Correo: ")

for usuario in datos["usuarios"]:
    if usuario["correo"] == correo_ingresado:
        print("Correo encontrado")