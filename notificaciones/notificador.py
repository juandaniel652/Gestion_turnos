from abc import ABC, abstractmethod

class Notificador (ABC) :

    @abstractmethod
    def notificar(self, cliente, turno) :

        pass


class NotificadorEmail (Notificador) :

    def notificar(self, cliente, turno) :

        print(f"[EMAIL] Enviando email a {cliente.contacto} con el turno: {turno}")


class NotificadorWhatsApp (Notificador) :

    def notificar(self, cliente, turno) :

        print(f"[WHATSAPP] Enviando mensaje de WhatsApp a {cliente.contacto} con el turno: {turno}")
