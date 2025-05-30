# -*- coding: utf-8 -*-
import pickle
import os
from modelos.paciente import Paciente

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
        if not self.pacientes:
            print("No hay pacientes cargados.")
        for p in self.pacientes:
            print(p)

    def buscar_por_dni(self, dni):
        for p in self.pacientes:
            if p.dni == dni:
                return p
        return None

    def agregar(self, dni, nombre, fecha_nacimiento, obra_social=""):
        if self.buscar_por_dni(dni):
            print("Ya existe un paciente con ese DNI.")
            return
        nuevo = Paciente(dni, nombre, fecha_nacimiento, obra_social)
        self.pacientes.append(nuevo)
        print("Paciente agregado.")

    def modificar(self, dni, nuevo_nombre=None, nueva_obra_social=None, nueva_fecha=None):
        paciente = self.buscar_por_dni(dni)
        if paciente:
            if nuevo_nombre:
                paciente.nombre = nuevo_nombre
            if nueva_obra_social is not None:
                paciente.obra_social = nueva_obra_social
            if nueva_fecha:
                paciente.fecha_nacimiento = nueva_fecha
            print("Paciente modificado.")
        else:
            print("Paciente no encontrado.")

    def eliminar(self, dni):
        paciente = self.buscar_por_dni(dni)
        if paciente:
            self.pacientes.remove(paciente)
            print("Paciente eliminado.")
        else:
            print("Paciente no encontrado.")

def menu_pacientes():
    gestor = GestorDePacientes()
    while True:
        print("\n📋 Gestión de Pacientes")
        print("1. Listar todos")
        print("2. Buscar por DNI")
        print("3. Agregar")
        print("4. Modificar")
        print("5. Eliminar")
        print("6. Guardar cambios")
        print("0. Volver al menú principal")

        opcion = input("Elija una opción: ")
        if opcion == "1":
            gestor.listar_todos()
        elif opcion == "2":
            dni = input("DNI del paciente: ")
            paciente = gestor.buscar_por_dni(dni)
            print(paciente if paciente else "No encontrado.")
        elif opcion == "3":
            dni = input("DNI: ")
            nombre = input("Nombre: ")
            fecha = input("Fecha de nacimiento (dd/mm/aaaa): ")
            obra = input("Obra social (opcional): ")
            gestor.agregar(dni, nombre, fecha, obra)
        elif opcion == "4":
            dni = input("DNI a modificar: ")
            nombre = input("Nuevo nombre (enter para dejar igual): ")
            obra = input("Nueva obra social (enter para dejar igual): ")
            fecha = input("Nueva fecha de nacimiento (dd/mm/aaaa o enter): ")
            gestor.modificar(dni,
                             nuevo_nombre=nombre if nombre else None,
                             nueva_obra_social=obra if obra else None,
                             nueva_fecha=fecha if fecha else None)
        elif opcion == "5":
            dni = input("DNI a eliminar: ")
            gestor.eliminar(dni)
        elif opcion == "6":
            gestor.guardar()
            print("Cambios guardados.")
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")
