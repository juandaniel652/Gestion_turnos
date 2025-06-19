class Turno :
    def __init__ (self, id_turno, cliente, servicio, fecha, hora) :

        self.id_turno = id_turno
        self.cliente = cliente
        self.servicio = servicio
        self.fecha = fecha
        self.hora = hora

    def __str__ (self) :
        
        return (f"Turno {self.id_turno}: {self.cliente.nombre} - "
                f"{self.servicio.nombre} - {self.fecha} {self.hora}")
