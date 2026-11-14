# Clínica ACME

Aplicación de consola para gestionar usuarios, pacientes, diagnósticos, prescripciones e historias clínicas. El proyecto está desarrollado en Python y almacena sus datos en archivos JSON.

## Requisitos

- Python 3.10 o posterior.
- No requiere instalar paquetes externos; utiliza módulos incluidos en Python.

## Ejecución

Abre una terminal en la carpeta del proyecto y ejecuta:

```bash
python3 main.py
```

Inicia sesión con el usuario administrador inicial:

- Correo: `admin@acmeclinic.com`
- Contraseña: `admin123`

## Funciones

- Acceso con correo y contraseña.
- Gestión de usuarios: agregar, modificar y eliminar usuarios. Los roles disponibles son `administrativo`, `medico` o `ambos`.
- Gestión de pacientes: agregar y modificar pacientes.
- Diagnóstico para usuarios con rol médico: registrar síntomas, diagnóstico y uno o más medicamentos con cantidad, dosis diaria y duración en días.
- Generación de un archivo JSON de prescripción por diagnóstico, asociado a la fecha, el paciente y el médico.
- Consulta de historia clínica por identificación, con opción de ver toda la historia o buscar consultas por fecha.

## Estructura

```text
Proyecto_Python_ArauzCarlos/
├── main.py
├── README.md
├── datos/
│   ├── clinica.json
│   └── prescripcion_*.json
└── modulos/
    ├── diagnosticos.py
    ├── esperas.py
    ├── historia.py
    ├── pacientes.py
    ├── usuarios.py
    └── validaciones.py
```

`clinica.json` guarda usuarios, pacientes y consultas. Cada prescripción generada se guarda como un archivo JSON separado dentro de `datos/`.

## Nota académica

Este proyecto es una aplicación de práctica. Las contraseñas se almacenan como texto en el archivo JSON, por lo que no debe utilizarse para guardar credenciales reales.
