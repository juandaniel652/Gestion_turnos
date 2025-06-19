import customtkinter as ctk
from tkinter import messagebox

class TurnoForm(ctk.CTkFrame):
    def __init__(self, master, gestor, clientes, servicios):
        super().__init__(master)
        self.gestor = gestor
        self.clientes = clientes
        self.servicios = servicios

        self.label = ctk.CTkLabel(self, text="Asignar Nuevo Turno", font=ctk.CTkFont(size=20, weight="bold"))
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

        self.combo_cliente = ctk.CTkComboBox(self, values=[c.nombre for c in clientes])
        self.combo_cliente.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        ctk.CTkLabel(self, text="Cliente:").grid(row=1, column=0, padx=5, sticky="w")

        self.combo_servicio = ctk.CTkComboBox(self, values=[s.nombre for s in servicios])
        self.combo_servicio.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        ctk.CTkLabel(self, text="Servicio:").grid(row=2, column=0, padx=5, sticky="w")

        self.fecha = ctk.CTkEntry(self, placeholder_text="YYYY-MM-DD")
        self.fecha.grid(row=3, column=1, padx=5, pady=5, sticky="ew")
        ctk.CTkLabel(self, text="Fecha:").grid(row=3, column=0, padx=5, sticky="w")

        self.hora = ctk.CTkEntry(self, placeholder_text="HH:MM")
        self.hora.grid(row=4, column=1, padx=5, pady=5, sticky="ew")
        ctk.CTkLabel(self, text="Hora:").grid(row=4, column=0, padx=5, sticky="w")

        self.btn_asignar = ctk.CTkButton(self, text="Asignar Turno", command=self.asignar_turno)
        self.btn_asignar.grid(row=5, column=0, columnspan=2, pady=10)

        self.columnconfigure(1, weight=1)

    def asignar_turno(self):
        cliente_idx = self.combo_cliente.get()
        servicio_idx = self.combo_servicio.get()
        fecha = self.fecha.get().strip()
        hora = self.hora.get().strip()

        cliente = next((c for c in self.clientes if c.nombre == cliente_idx), None)
        servicio = next((s for s in self.servicios if s.nombre == servicio_idx), None)

        if not cliente or not servicio:
            messagebox.showwarning("Datos faltantes", "Seleccione cliente y servicio.")
            return

        turno = self.gestor.asignar_turno(cliente, servicio, fecha, hora)
        if turno:
            messagebox.showinfo("Éxito", "Turno asignado correctamente.")
            self.fecha.delete(0, "end")
            self.hora.delete(0, "end")


class TurnoLista(ctk.CTkFrame):
    def __init__(self, master, gestor):
        super().__init__(master)
        self.gestor = gestor

        label = ctk.CTkLabel(self, text="Turnos asignados", font=ctk.CTkFont(size=18, weight="bold"))
        label.pack(pady=5)

        self.texto = ctk.CTkTextbox(self, height=200)
        self.texto.pack(fill="both", expand=True, padx=10, pady=5)

        self.entry_id = ctk.CTkEntry(self, placeholder_text="ID de turno a eliminar")
        self.entry_id.pack(pady=5)

        self.btn_eliminar = ctk.CTkButton(self, text="Eliminar Turno", command=self.eliminar_turno)
        self.btn_eliminar.pack(pady=3)

        self.btn_exportar = ctk.CTkButton(self, text="Exportar a Excel", command=self.exportar)
        self.btn_exportar.pack(pady=3)

        self.actualizar_lista()

    def actualizar_lista(self):
        self.texto.configure(state="normal")
        self.texto.delete("1.0", "end")
        if not self.gestor.turnos:
            self.texto.insert("end", "No hay turnos registrados.\n")
        else:
            for t in self.gestor.turnos:
                self.texto.insert("end", str(t) + "\n")
        self.texto.configure(state="disabled")

    def eliminar_turno(self):
        turno_id = self.entry_id.get().strip()
        if self.gestor.eliminar_turno(turno_id):
            messagebox.showinfo("Eliminado", "Turno eliminado correctamente.")
            self.actualizar_lista()
        else:
            messagebox.showerror("Error", "No se encontró el ID.")

    def exportar(self):
        self.gestor.exportar_a_excel()
        messagebox.showinfo("Exportación", "Turnos exportados exitosamente.")
