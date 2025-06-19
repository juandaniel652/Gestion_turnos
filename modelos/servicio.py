class Servicio :
    def __init__ (self, id_servicio, nombre, duracion_min) :

        self.id_servicio = id_servicio
        self.nombre = nombre
        self.duracion_min = duracion_min

    def __str__ (self) :
        
        return f"{self.nombre} ({self.duracion_min} min)"
