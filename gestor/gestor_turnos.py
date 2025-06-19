import re
import openpyxl
from modelos.turno import Turno
from utils.generador_id import generar_id_turno
from utils.persistencia import guardar_turnos_json, cargar_turnos_json


class GestorTurnos :

    def __init__ (self, notificador) :

        self.notificador = notificador  # Estrategia de notificación
        self.turnos = cargar_turnos_json()  # Carga los turnos desde JSON


    def obtener_turnos_por_fecha (self, fecha) :

        return [turno for turno in self.turnos if turno.fecha == fecha]


    def verificar_disponibilidad (self, fecha, hora) :

        return not any(turno.fecha == fecha and turno.hora == hora for turno in self.turnos)


    def validar_fecha (self, fecha) :

        return re.match(r"^\d{4}-\d{2}-\d{2}$", fecha)


    def validar_hora (self, hora) :

        return re.match(r"^\d{2}:\d{2}$", hora)


    def asignar_turno (self, cliente, servicio, fecha, hora) :

        if not self.validar_fecha (fecha) :

            print("❌ Formato de fecha inválido. Use AAAA-MM-DD.")
            return None

        if not self.validar_hora (hora) :

            print("❌ Formato de hora inválido. Use HH:MM.")
            return None

        if not self.verificar_disponibilidad (fecha, hora) :

            print(f"❌ Ya hay un turno para {fecha} a las {hora}.")
            return None

        id_turno = generar_id_turno()
        nuevo_turno = Turno(id_turno, cliente, servicio, fecha, hora)
        self.turnos.append(nuevo_turno)

        guardar_turnos_json(self.turnos)
        self.notificador.notificar(cliente, nuevo_turno)

        print(f"✅ Turno asignado: {nuevo_turno}")
        return nuevo_turno
    

    def eliminar_turno (self, id_turno) :

        for indice, turno in enumerate (self.turnos) :

            if turno.id_turno == id_turno :

                eliminado = self.turnos.pop(indice)
                guardar_turnos_json(self.turnos)
                print(f"🗑️ Turno eliminado: {eliminado}")
                return True
            
        print(f"❌ No se encontró ningún turno con ID {id_turno}")
        return False


    def exportar_a_excel (self, nombre_archivo = "turnos_exportados.xlsx") :

        libro_de_trabajo = openpyxl.Workbook()
        hojas_de_trabajo = libro_de_trabajo.active
        hojas_de_trabajo.title = "Turnos"

        hojas_de_trabajo.append(["ID", "Cliente", "Servicio", "Fecha", "Hora"])

        for turno in self.turnos :

            hojas_de_trabajo.append([
                turno.id_turno,
                turno.cliente.nombre,
                turno.servicio.nombre,
                turno.fecha,
                turno.hora
            ])

        libro_de_trabajo.save(nombre_archivo)
        print(f"📁 Turnos exportados exitosamente a '{nombre_archivo}'.")


    def mostrar_turnos (self) :

        if not self.turnos :

            print("📭 No hay turnos asignados.")

        else :
            
            for turno in self.turnos :

                print(turno)
