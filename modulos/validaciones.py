from datetime import datetime


def pedir_texto(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor != "":
            return valor
        print("Este campo es obligatorio.")


def pedir_rol(mensaje, permitir_vacio=False):
    while True:
        rol = input(mensaje).strip().lower()

        if permitir_vacio and rol == "":
            return ""
        if rol == "médico":
            rol = "medico"
        if rol in ("administrativo", "medico", "ambos"):
            return rol

        print("Rol no válido. Escribe administrativo, medico o ambos.")


def pedir_si_no(mensaje):
    while True:
        respuesta = input(mensaje).strip().lower()
        if respuesta in ("si", "sí"):
            return "si"
        if respuesta == "no":
            return "no"
        print("Respuesta no válida. Escribe si o no.")


def pedir_dias(mensaje):
    while True:
        try:
            dias = int(input(mensaje))
            if dias > 0:
                return dias
            print("La duración debe ser mayor que cero.")
        except ValueError:
            print("Escribe un número entero de días, por ejemplo: 5.")


def pedir_fecha(mensaje):
    while True:
        fecha = input(mensaje).strip()
        try:
            datetime.strptime(fecha, "%Y-%m-%d")
            return fecha
        except ValueError:
            print("Fecha no válida. Usa el formato AAAA-MM-DD, por ejemplo 2026-11-13.")


def esperar_volver(mensaje):
    while True:
        opcion = input(mensaje).strip()
        if opcion == "1":
            return
        print("Opción inválida. Solo puedes ingresar 1.")
