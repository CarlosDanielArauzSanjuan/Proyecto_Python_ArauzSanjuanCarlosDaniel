def mostrar_datos_paciente(paciente):
    print("\n╔══════════════════════════════════════╗")
    print("║             DATOS DEL PACIENTE       ║")
    print("╠══════════════════════════════════════╣")
    print("║ Identificación:", paciente["identificacion"])
    print("║ Nombres:", paciente["nombres"])
    print("║ Apellidos:", paciente["apellidos"])
    print("║ Teléfono:", paciente["telefono"])
    print("║ Correo:", paciente["correo"])
    print("║ Dirección:", paciente["direccion"])
    print("║ Género:", paciente["genero"])
    print("║ Estado civil:", paciente["estado_civil"])
    print("╚══════════════════════════════════════╝")


def mostrar_consulta(consulta):
    print("\n╔══════════════════════════════════════╗")
    print("║                CONSULTA               ║")
    print("╠══════════════════════════════════════╣")
    print("║ Fecha:", consulta["fecha"])
    print("║ Médico:", consulta["medico"])
    print("║ Síntomas:", consulta["sintomas"])
    print("║ Diagnóstico:", consulta["diagnostico"])
    print("║ Medicamentos:")

    for medicamento in consulta["medicamentos"]:
        print("  -", medicamento["medicamento"])
        print("    Cantidad:", medicamento["cantidad"])
        print("    Dosis diaria:", medicamento["dosis"])
        print("    Duración en días:", medicamento["tiempo_dias"])


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

    while True:
        print("\n╔══════════════════════════════════════╗")
        print("║             HISTORIA CLÍNICA         ║")
        print("╠══════════════════════════════════════╣")
        print(" Paciente:", paciente["nombres"], paciente["apellidos"])
        print("\n║ 1. Ver historia completa             ║")
        print("║ 2. Buscar consulta por fecha         ║")
        print("║ 0. Volver al menú principal          ║")
        print("╚══════════════════════════════════════╝")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            mostrar_datos_paciente(paciente)
            historial_encontrado = False

            for consulta in datos["consultas"]:
                if consulta["identificacion_paciente"] == identificacion:
                    historial_encontrado = True
                    mostrar_consulta(consulta)

            if historial_encontrado == False:
                print("Este paciente todavía no tiene consultas registradas.")

        elif opcion == "2":
            fechas_encontradas = False
            print("Fechas disponibles:")

            for consulta in datos["consultas"]:
                if consulta["identificacion_paciente"] == identificacion:
                    fechas_encontradas = True
                    print("-", consulta["fecha"])

            if fechas_encontradas:
                fecha_buscada = input("Escribe la fecha exacta de la consulta: ")
                consulta_encontrada = False

                for consulta in datos["consultas"]:
                    if (consulta["identificacion_paciente"] == identificacion
                            and consulta["fecha"] == fecha_buscada):
                        consulta_encontrada = True
                        mostrar_datos_paciente(paciente)
                        mostrar_consulta(consulta)

                if consulta_encontrada == False:
                    print("No se encontró una consulta con esa fecha.")
            else:
                print("Este paciente todavía no tiene consultas registradas.")

        elif opcion == "0":
            break
        else:
            print("Opción inválida.")
