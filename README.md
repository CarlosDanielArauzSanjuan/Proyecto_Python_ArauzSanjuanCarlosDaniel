# 🏥 Clínica ACME

> Aplicación de consola para gestionar usuarios, pacientes, diagnósticos, prescripciones e historias clínicas.

**Proyecto académico · Python · Persistencia en JSON**

---

## 🧭 Contenido

- [Acerca del proyecto](#-acerca-del-proyecto)
- [Funciones](#-funciones)
- [Roles y permisos](#-roles-y-permisos)
- [Inicio rápido](#-inicio-rápido)
- [Estructura](#-estructura-del-proyecto)
- [Datos y archivos JSON](#-datos-y-archivos-json)
- [Validaciones](#-validaciones-de-entrada)
- [Seguridad](#-nota-de-seguridad)

## 💡 Acerca del proyecto

La aplicación digitaliza el registro básico de pacientes y consultas de la Clínica ACME. El personal autorizado puede administrar usuarios y pacientes, registrar diagnósticos y prescripciones, y consultar la historia clínica de cada paciente.

Los datos se guardan localmente en archivos JSON. El código está dividido en módulos para separar las distintas funciones de la aplicación.

## ✨ Funciones

- Acceso mediante correo electrónico y contraseña.
- Registro, modificación y eliminación de usuarios operativos.
- Registro y modificación de pacientes.
- Diagnóstico de pacientes previamente registrados.
- Registro de síntomas, diagnóstico y uno o más medicamentos por consulta.
- Generación de un archivo JSON para cada prescripción, asociado a su fecha, paciente y médico.
- Consulta de la historia completa de un paciente o búsqueda de sus consultas por fecha.
- Menús adaptados a los roles asignados a cada cuenta.

## 👥 Roles y permisos

Una cuenta puede tener un rol o ambos. Al registrar un usuario, escribe `administrativo`, `medico` o `ambos`.

| Función | Administrativo | Médico | Ambos |
|---|:---:|:---:|:---:|
| Gestionar usuarios | ✅ | — | ✅ |
| Agregar o modificar pacientes | ✅ | ✅ | ✅ |
| Registrar diagnósticos y prescripciones | — | ✅ | ✅ |
| Consultar historias clínicas | ✅ | ✅ | ✅ |

La identificación y el correo de los usuarios deben ser únicos. El sistema protege la cuenta administrativa inicial, la cuenta de la sesión actual y la última cuenta administrativa contra eliminación.

## 🚀 Inicio rápido

### Requisitos

- **Python 3.10 o posterior**, por el uso de `match/case`.
- No requiere paquetes externos.

### Ejecutar

Abre una terminal en la carpeta del proyecto y ejecuta:

```bash
cd Proyecto_Python_ArauzCarlos
python3 main.py
```

### Cuenta inicial

El archivo `datos/clinica.json` incluye el usuario administrativo inicial:

| Campo | Valor |
|---|---|
| Correo | `admin@acmeclinic.com` |
| Contraseña de práctica | `admin123` |
| Rol | Administrativo |

## 🧩 Estructura del proyecto

```text
Proyecto_Python_ArauzCarlos/
├── main.py
├── README.md
├── datos/
│   ├── clinica.json
│   └── prescripcion_*.json
└── modulos/
    ├── diagnosticos.py
    ├── historia.py
    ├── pacientes.py
    ├── usuarios.py
    └── validaciones.py
```

| Archivo | Responsabilidad |
|---|---|
| `main.py` | Carga los datos, valida el acceso y presenta el menú según los roles. |
| `modulos/usuarios.py` | Agrega, modifica y elimina usuarios. |
| `modulos/pacientes.py` | Agrega y modifica pacientes. |
| `modulos/diagnosticos.py` | Registra consultas y genera los archivos de prescripción. |
| `modulos/historia.py` | Muestra los datos del paciente y consulta su historial. |
| `modulos/validaciones.py` | Comprueba campos, roles, fechas, duración, respuestas y opciones de regreso. |
| `datos/clinica.json` | Almacena usuarios, pacientes y consultas. |

## 🗃 Datos y archivos JSON

`datos/clinica.json` contiene tres listas principales:

| Lista | Contenido |
|---|---|
| `usuarios` | Datos del personal, contraseña y lista de roles. |
| `pacientes` | Identificación, nombres, apellidos, contacto, dirección, género y estado civil. |
| `consultas` | Fecha, paciente, médico, síntomas, diagnóstico y medicamentos. |

Cada medicamento guarda su nombre, cantidad, dosis diaria y duración en días. Además de la consulta almacenada en `clinica.json`, al completar el diagnóstico se crea un archivo `prescripcion_*.json` dentro de `datos/`.

## ✅ Validaciones de entrada

- Los campos obligatorios no aceptan texto vacío.
- Los roles aceptan mayúsculas o minúsculas; `Médico` también se normaliza a `medico`.
- La duración del tratamiento debe ser un número entero mayor que cero.
- Para agregar otro medicamento se acepta `si`, `sí` o `no`, sin importar las mayúsculas.
- Las fechas de consulta se ingresan como `AAAA-MM-DD`.
- Las opciones inválidas muestran un aviso y vuelven a solicitar la entrada.
- Después de mostrar resultados, la aplicación espera la opción de regreso antes de redibujar el menú.

## 🔐 Nota de seguridad

Este es un proyecto académico. Las contraseñas se guardan como texto en el JSON; no uses este método para almacenar credenciales reales ni para operar un sistema clínico en producción.
