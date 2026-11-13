def consultar_historia(datos):
    identificacion = input("Identificación del paciente: ")

    paciente_encontrado = False

    for paciente in datos["pacientes"]:
        if paciente["identificacion"] == identificacion:
            paciente_encontrado = True
            break

    if paciente_encontrado == False:
        print("Paciente no encontrado.")
        return

    print("\n======= Datos del paciente =======")
    print("Identificación:", paciente["identificacion"])
    print("Nombres:", paciente["nombres"])
    print("Apellidos:", paciente["apellidos"])
    print("Teléfono:", paciente["telefono"])
    print("Correo:", paciente["correo"])
    print("Dirección:", paciente["direccion"])
    print("Género:", paciente["genero"])
    print("Estado civil:", paciente["estado_civil"])

    historial_encontrado = False

    for consulta in datos["consultas"]:
        if consulta["identificacion_paciente"] == identificacion:
            historial_encontrado = True

            print("\n======= Consulta =======")
            print("Fecha:", consulta["fecha"])
            print("Médico:", consulta["medico"])
            print("Síntomas:", consulta["sintomas"])
            print("Diagnóstico:", consulta["diagnostico"])
            print("Medicamentos:")

            for medicamento in consulta["medicamentos"]:
                print("- Medicamento:", medicamento["medicamento"])
                print("  Cantidad:", medicamento["cantidad"])
                print("  Dosis diaria:", medicamento["dosis"])
                print("  Duración en días:", medicamento["tiempo_dias"])

    if historial_encontrado == False:
        print("\nEste paciente todavía no tiene consultas registradas.")