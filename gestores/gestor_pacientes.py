# -*- coding: utf-8 -*-

import os
from modelos.paciente import Paciente
from utils.fecha import Fecha
from utils.persistencia import Persistencia  

class GestorDePacientes:
    def __init__(self, archivo='datos/pacientes.bin'):
        self.archivo = archivo
        self.pacientes = Persistencia.cargar(self.archivo)

    def guardar(self):
        Persistencia.guardar(self.archivo, self.pacientes)

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

    def agregar(self):
        dni = input("DNI: ")
        if self.buscar_por_dni(dni):
            print("Ya existe un paciente con ese DNI.")
            return
        nombre = input("Nombre: ")
        fecha_nacimiento = self._pedir_fecha_de_nacimiento_valida()
        obra_social = input("Obra social (opcional): ")
        try:
            nuevo = Paciente(dni, nombre, fecha_nacimiento, obra_social)        
        except ValueError as e:
            print("Error al crear el paciente.", e)
            return

        self.pacientes.append(nuevo)
        print("Paciente agregado.")

    def modificar(self):
        dni = input("DNI a modificar: ")
        paciente = self.buscar_por_dni(dni)
        if paciente:
            nuevo_nombre = input("Nuevo nombre (enter para dejar igual): ")
            nueva_obra_social = input("Nueva obra social (enter para dejar igual): ")
            nueva_fecha = input("Nueva fecha de nacimiento (dd/mm/aaaa o enter): ")
            if nuevo_nombre:
                paciente.nombre = nuevo_nombre
            if nueva_obra_social:
                paciente.obra_social = nueva_obra_social
            if nueva_fecha:
                try:
                    paciente.fecha_nacimiento = Fecha(nueva_fecha)
                except ValueError as e:
                    print(e)
            print("Paciente modificado.")
        else:
            print("Paciente no encontrado.")

    def eliminar(self):
        dni = input("DNI a eliminar: ")
        paciente = self.buscar_por_dni(dni)
        if paciente:
            self.pacientes.remove(paciente)
            print("Paciente eliminado.")
        else:
            print("Paciente no encontrado.")

    def _pedir_fecha_de_nacimiento_valida(self):
        while True:
            fecha_str = input("Fecha de nacimiento (dd/mm/aaaa): ").strip()
            try:
                return Fecha(fecha_str)
            except ValueError as e:
                print(e)

    def limpiar_pantalla(self):    
        os.system('cls' if os.name == 'nt' else 'clear')       

def menu_pacientes():
    gestor = GestorDePacientes()
    gestor.limpiar_pantalla()        
    while True:        
        print("\nGestión de Pacientes")
        print("1. Listar todos")
        print("2. Buscar por DNI")
        print("3. Agregar")
        print("4. Modificar")
        print("5. Eliminar")
        print("6. Guardar cambios")
        print("7. Limpiar pantalla")
        print("0. Volver al menú principal")

        opcion = input("Elija una opción: ")
        if opcion == "1":
            gestor.listar_todos()
        elif opcion == "2":
            dni = input("DNI del paciente: ")
            paciente = gestor.buscar_por_dni(dni)
            print(paciente if paciente else "No encontrado.")
        elif opcion == "3":
            gestor.agregar()
        elif opcion == "4":
            gestor.modificar()
        elif opcion == "5":
            gestor.eliminar()
        elif opcion == "6":
            gestor.guardar()
            print("Cambios guardados.")
        elif opcion == "7":
            gestor.limpiar_pantalla()
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")