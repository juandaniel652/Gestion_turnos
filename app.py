import customtkinter as ctk
from modelos.cliente import Cliente
from modelos.servicio import Servicio
from gestor.gestor_turnos import GestorTurnos
from notificaciones.notificador import NotificadorEmail
from interfaz.vistas import TurnoForm, TurnoLista

# Datos de prueba
nombres_emails = [
    ("Ana Torres", "ana@email.com"),
    ("Carlos Díaz", "carlos@wapp.com"),
    ("Lucía Gómez", "lucia.gomez@mail.com"),
    ("Miguel Pérez", "miguel.perez@mail.com"),
    ("Sofía Ramírez", "sofia.ramirez@mail.com"),
    ("Javier López", "javier.lopez@mail.com"),
    ("Marina Fernández", "marina.fernandez@mail.com"),
    ("Pedro Sánchez", "pedro.sanchez@mail.com"),
    ("Laura Ruiz", "laura.ruiz@mail.com"),
    ("Diego Castro", "diego.castro@mail.com"),
]

servicios_nombres_duracion = [
    ("Corte de cabello", 30),
    ("Coloración", 60),
    ("Peinado", 45),
    ("Manicura", 40),
    ("Pedicura", 50),
    ("Depilación", 35),
    ("Masaje", 60),
    ("Tratamiento facial", 55),
    ("Barba", 20),
    ("Alisado", 90),
]

clientes = [
    Cliente(f"{i+1:03}", nombre, email)
    for i, (nombre, email) in enumerate(nombres_emails)
]


servicios = [
    Servicio(f"S{i+1:02}", nombre, duracion)
    for i, (nombre, duracion) in enumerate(servicios_nombres_duracion)
]

class AppTurnos(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("dark")  # dark | light | system
        ctk.set_default_color_theme("blue")  # también: green, dark-blue

        self.title("💈 Gestor de Turnos")
        self.geometry("700x550")
        self.gestor = GestorTurnos(NotificadorEmail())

        self.formulario = TurnoForm(self, self.gestor, clientes, servicios)
        self.formulario.pack(pady=15, padx=15, fill="x")

        self.lista = TurnoLista(self, self.gestor)
        self.lista.pack(pady=15, padx=15, fill="both", expand=True)

        actualizar_btn = ctk.CTkButton(self, text="🔄 Actualizar Lista", command=self.lista.actualizar_lista)
        actualizar_btn.pack(pady=10)

if __name__ == "__main__":
    app = AppTurnos()
    app.mainloop()
