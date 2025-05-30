import pickle
import os
from modelos.paciente import Paciente
from modelos.fechahora import FechaHora

class GestorDePacientes:
    def __init__(self, archivo='datos/pacientes.bin'):
        self.archivo = archivo
        self.pacientes = []
        self.cargar()

    def cargar(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, 'rb') as f:
                self.pacientes = pickle.load(f)
        else:
            self.pacientes = []

    def guardar(self):
        with open(self.archivo, 'wb') as f:
            pickle.dump(self.pacientes, f)

    def listar_todos(self):
        for paciente in self.pacientes:
            print(paciente)

    def buscar_por_dni(self, dni):
        for paciente in self.pacientes:
            if paciente.dni == dni:
                return paciente
        return None

    def agregar(self, dni, nombre, fecha_str, obra_social=""):
        if self.buscar_por_dni(dni):
            print("Ya existe un paciente con ese DNI.")
            return
        fecha_nacimiento = FechaHora(fecha_str, "00:00")  # Solo usamos la fecha
        nuevo = Paciente(dni, nombre, fecha_nacimiento, obra_social)
        self.pacientes.append(nuevo)
        print("Paciente agregado.")

    def modificar(self, dni, nuevo_nombre=None, nueva_obra_social=None, nueva_fecha=None):
        paciente = self.buscar_por_dni(dni)
        if not paciente:
            print("Paciente no encontrado.")
            return
        if nuevo_nombre:
            paciente.nombre = nuevo_nombre
        if nueva_obra_social is not None:
            paciente.obra_social = nueva_obra_social
        if nueva_fecha:
            paciente.fecha_nacimiento = FechaHora(nueva_fecha, "00:00")
        print("Paciente modificado.")

    def eliminar(self, dni):
        paciente = self.buscar_por_dni(dni)
        if paciente:
            self.pacientes.remove(paciente)
            print("Paciente eliminado.")
        else:
            print("Paciente no encontrado.")
