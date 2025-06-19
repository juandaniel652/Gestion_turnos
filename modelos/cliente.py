class Cliente :

    def __init__ (self, id_cliente, nombre, contacto) :

        self.id_cliente = id_cliente
        self.nombre = nombre
        self.contacto = contacto

    def __str__ (self) :
        
        return f"{self.nombre} (ID: {self.id_cliente})"
