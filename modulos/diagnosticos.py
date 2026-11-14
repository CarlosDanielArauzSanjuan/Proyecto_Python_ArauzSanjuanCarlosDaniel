import json
from datetime import datetime
from pathlib import Path


def diagnosticar_paciente(datos, usuario, ruta):
    identificacion_paciente = input("Identificación del paciente: ")

    paciente_encontrado = False

    for paciente in datos["pacientes"]:
        if paciente["identificacion"] == identificacion_paciente:
            paciente_encontrado = True
            break

    if paciente_encontrado == False:
        print("Paciente no encontrado. Debe registrarse primero.")
        return

    sintomas = input("Síntomas: ")
    diagnostico = input("Diagnóstico: ")

    medicamentos = []
    agregar_medicamento = "s"

    while agregar_medicamento == "s":
        medicamento = input("Medicamento: ")
        cantidad = input("Cantidad (por ejemplo, 20 tabletas): ")
        dosis = input("Dosis diaria: ")
        while True:
            try:
                tiempo_dias = int(input("Duración del tratamiento en días: "))
                if tiempo_dias > 0:
                    break
                print("La duración debe ser mayor que cero.")
            except ValueError:
                print("Escribe un número entero de días, por ejemplo: 5.")

        nuevo_medicamento = {
            "medicamento": medicamento,
            "cantidad": cantidad,
            "dosis": dosis,
            "tiempo_dias": tiempo_dias
        }

        medicamentos.append(nuevo_medicamento)
        agregar_medicamento = input("¿Agregar otro medicamento? (s/n): ")

    fecha_hora = datetime.now()
    fecha_consulta = fecha_hora.strftime("%Y-%m-%d %H:%M:%S")

    consulta = {
        "fecha": fecha_consulta,
        "identificacion_paciente": paciente["identificacion"],
        "paciente": paciente["nombres"] + " " + paciente["apellidos"],
        "identificacion_medico": usuario["identificacion"],
        "medico": usuario["nombres"] + " " + usuario["apellidos"],
        "sintomas": sintomas,
        "diagnostico": diagnostico,
        "medicamentos": medicamentos
    }

    datos["consultas"].append(consulta)

    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4)

    fecha_para_archivo = fecha_hora.strftime("%Y%m%d_%H%M%S_%f")
    nombre_archivo = "prescripcion_" + fecha_para_archivo + ".json"

    ruta_prescripcion = Path(ruta).parent / nombre_archivo

    with open(ruta_prescripcion, "w", encoding="utf-8") as archivo:
        json.dump(consulta, archivo, indent=4)

    print("Consulta registrada.")
    print("Prescripción guardada en:", ruta_prescripcion)
