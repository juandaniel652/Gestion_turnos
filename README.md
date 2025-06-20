# Gestion_turnos
Programa de reserva de turnos
# 🗓️ Gestor de Turnos - Proyecto Final Python

Este es un sistema de gestión de turnos desarrollado en Python, que permite asignar, visualizar, eliminar y exportar turnos de forma automatizada. Incluye una interfaz gráfica amigable con Tkinter, almacenamiento persistente en JSON y exportación a Excel.

## 📌 Características

- 📇 Asignación de turnos con cliente, servicio, fecha y hora.
- ✅ Validaciones de formato de fecha y disponibilidad.
- 🧠 Programación Orientada a Objetos (POO) con herencia y polimorfismo.
- 📦 Persistencia de datos en archivo JSON.
- 📤 Exportación de turnos a archivo Excel (.xlsx).
- 🔔 Sistema de notificaciones modular (estrategia de diseño).
- 🖥️ Interfaz gráfica desarrollada con CustomTkinter.

---

## 🛠️ Tecnologías utilizadas

- Python 3.11
- CustomTkinter (GUI)
- openpyxl (Excel)
- JSON (persistencia)
- POO (Clases, Herencia, Polimorfismo)
- Patrones de diseño (Strategy)

---

## 🧩 Estructura del proyecto

gestor_turnos/
├── app.py                          # Ejecutable principal de la app GUI (CustomTkinter)
│
├── modelos/                        # Clases del modelo del dominio (POO)
│   ├── cliente.py                 # Clase Cliente con herencia
│   ├── servicio.py                # Clase Servicio
│   └── turno.py                   # Clase Turno que relaciona cliente y servicio
│
├── gestor/                         # Lógica del negocio
│   └── gestor_turnos.py           # Clase GestorTurnos: asigna, valida y administra turnos
│
├── notificaciones/                 # Implementación del patrón Strategy
│   ├── notificador.py             # Interfaz y estrategias de notificación (simulación por email)
│
├── interfaz/                       # Interfaz gráfica de usuario
│   ├── app.py                     # Ventana principal
│   ├── vistas.py                  # Componentes visuales: formulario y lista de turnos
│   
│
├── utils/                          # Funciones auxiliares y persistencia
│   ├── persistencia.py            # Guardado y carga de turnos en JSON
│   ├── generador_id.py            # Generador automático de IDs únicos
│
├── datos/                          # Carpeta para persistencia de datos
│   └── turnos.json                # Archivo donde se guardan los turnos asignados
│
├── turnos_exportados.xlsx          # Archivo Excel generado al exportar turnos
│
└── README.md                       # Documentación del proyecto

