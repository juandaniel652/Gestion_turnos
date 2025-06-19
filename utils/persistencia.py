import json
from modelos.turno import Turno
from modelos.cliente import Cliente
from modelos.servicio import Servicio

def guardar_turnos_json(turnos, ruta="datos/turnos.json"):
    datos = []
    for t in turnos:
        datos.append({
            "id_turno": t.id_turno,
            "cliente": {
                "id_cliente": t.cliente.id_cliente,
                "nombre": t.cliente.nombre,
                "contacto": t.cliente.contacto
            },
            "servicio": {
                "id_servicio": t.servicio.id_servicio,
                "nombre": t.servicio.nombre,
                "duracion_min": t.servicio.duracion_min
            },
            "fecha": t.fecha,
            "hora": t.hora
        })
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4)

def cargar_turnos_json(ruta="datos/turnos.json"):
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            datos = json.load(f)
        turnos = []
        for d in datos:
            cliente = Cliente(**d["cliente"])
            servicio = Servicio(**d["servicio"])
            turno = Turno(d["id_turno"], cliente, servicio, d["fecha"], d["hora"])
            turnos.append(turno)
        return turnos
    except FileNotFoundError:
        return []

def cargar_turnos_json(ruta="datos/turnos.json"):
    import os
    if not os.path.exists(ruta):
        return []

    try:
        with open(ruta, "r", encoding="utf-8") as f:
            contenido = f.read().strip()
            if not contenido:
                return []  # Archivo vacío
            datos = json.loads(contenido)
    except (json.JSONDecodeError, FileNotFoundError):
        print("⚠️ Archivo de turnos vacío o corrupto. Se inicializa vacío.")
        return []

    turnos = []
    for d in datos:
        cliente = Cliente(**d["cliente"])
        servicio = Servicio(**d["servicio"])
        turno = Turno(d["id_turno"], cliente, servicio, d["fecha"], d["hora"])
        turnos.append(turno)
    return turnos
