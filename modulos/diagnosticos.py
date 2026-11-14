import json
from datetime import datetime
from pathlib import Path
from modulos.validaciones import esperar_volver, pedir_dias, pedir_si_no, pedir_texto


def diagnosticar_paciente(datos, usuario, ruta):
    identificacion_paciente = pedir_texto("Identificación del paciente: ")

    paciente_encontrado = False

    for paciente in datos["pacientes"]:
        if paciente["identificacion"] == identificacion_paciente:
            paciente_encontrado = True
            break

    if paciente_encontrado == False:
        print("Paciente no encontrado. Debe registrarse primero.")
        esperar_volver("1. Volver al menú principal: ")
        return

    sintomas = pedir_texto("Síntomas: ")
    diagnostico = pedir_texto("Diagnóstico: ")

    medicamentos = []

    while True:
        medicamento = pedir_texto("Medicamento: ")
        cantidad = pedir_texto("Cantidad (por ejemplo, 20 tabletas): ")
        dosis = pedir_texto("Dosis diaria: ")
        tiempo_dias = pedir_dias("Duración del tratamiento en días: ")

        nuevo_medicamento = {
            "medicamento": medicamento,
            "cantidad": cantidad,
            "dosis": dosis,
            "tiempo_dias": tiempo_dias
        }

        medicamentos.append(nuevo_medicamento)
        agregar_medicamento = pedir_si_no("¿Agregar otro medicamento? (si/no): ")
        if agregar_medicamento == "no":
            break

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
    esperar_volver("1. Volver al menú principal: ")
