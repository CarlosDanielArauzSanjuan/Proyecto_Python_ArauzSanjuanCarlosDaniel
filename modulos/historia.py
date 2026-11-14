from modulos.validaciones import esperar_volver, pedir_fecha, pedir_texto


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
    identificacion = pedir_texto("Identificación del paciente: ")
    paciente_encontrado = False

    for paciente in datos["pacientes"]:
        if paciente["identificacion"] == identificacion:
            paciente_encontrado = True
            break

    if paciente_encontrado == False:
        print("Paciente no encontrado.")
        esperar_volver("1. Volver al menú principal: ")
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

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            mostrar_datos_paciente(paciente)
            historial_encontrado = False

            for consulta in datos["consultas"]:
                if consulta["identificacion_paciente"] == identificacion:
                    historial_encontrado = True
                    mostrar_consulta(consulta)

            if historial_encontrado == False:
                print("Este paciente todavía no tiene consultas registradas.")
            esperar_volver("1. Volver al menú de historia clínica: ")

        elif opcion == "2":
            fechas_encontradas = False
            print("Fechas disponibles:")

            for consulta in datos["consultas"]:
                if consulta["identificacion_paciente"] == identificacion:
                    fechas_encontradas = True
                    print("-", consulta["fecha"])

            if fechas_encontradas:
                fecha_buscada = pedir_fecha("Escribe la fecha de la consulta (AAAA-MM-DD): ")
                consulta_encontrada = False

                for consulta in datos["consultas"]:
                    if (consulta["identificacion_paciente"] == identificacion
                            and consulta["fecha"].split(" ")[0] == fecha_buscada):
                        consulta_encontrada = True
                        mostrar_datos_paciente(paciente)
                        mostrar_consulta(consulta)

                if consulta_encontrada == False:
                    print("No se encontró una consulta con esa fecha.")
            else:
                print("Este paciente todavía no tiene consultas registradas.")
            esperar_volver("1. Volver al menú de historia clínica: ")

        elif opcion == "0":
            break
        else:
            print("Opción inválida.")
            esperar_volver("1. Volver al menú de historia clínica: ")
