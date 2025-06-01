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
            return

        print("=" * 80)
        print(f"{'DNI':<12} {'Nombre':<25} {'Obra Social':<20} {'Nacimiento':<15}")
        print("-" * 80)
        for p in self.pacientes:
            fecha_str = p.fecha_nacimiento.mi_fecha.strftime("%d/%m/%Y")
            print(f"{p.dni:<12} {p.nombre:<25} {p.obra_social:<20} {fecha_str:<15}")
        print("=" * 80)

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
        self.guardar()
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
            self.guardar()
            print("Paciente modificado.")
        else:
            print("Paciente no encontrado.")

    def eliminar(self):
        dni = input("DNI a eliminar: ")
        paciente = self.buscar_por_dni(dni)
        if paciente:
            confirmacion = input(f"¿Está seguro que desea eliminar al paciente {paciente.nombre} (DNI: {dni})? (S/N): ").strip().upper()
            if confirmacion == "S":
                self.pacientes.remove(paciente)
                self.guardar()
                print("Paciente eliminado.")
            else:
                print("Operación cancelada.")
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
        print("\n" + "="*40)
        print("🩺  \033[1mGestión de Pacientes\033[0m")
        print("="*40)
        print("[1] Listar todos")
        print("[2] Buscar por DNI")
        print("[3] Agregar")
        print("[4] Modificar")
        print("\033[31m[5] Eliminar\033[0m") 
        print("[6] Limpiar pantalla")
        print("[0] Volver al menú principal")
        print("="*40)

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
            gestor.limpiar_pantalla()
        elif opcion == "0":
            gestor.limpiar_pantalla()
            break
        else:
            print("Opción inválida.")