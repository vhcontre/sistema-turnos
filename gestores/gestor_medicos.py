# -*- coding: utf-8 -*-

import os
from modelos.medico import Medico
from utils.persistencia import Persistencia  
from utils.csv_handler import exportar_csv

class GestorDeMedicos:
    def __init__(self, archivo='datos/medicos.bin'):
        self.archivo = archivo
        self.medicos = Persistencia.cargar(self.archivo)  

    def guardar(self):
        Persistencia.guardar(self.archivo, self.medicos)  

    def exportar_datos_csv(self, archivo_csv='datos/medicos_exportados.csv'):
        if not self.medicos:
            print("No hay médicos para exportar.")
            return
        exportar_csv(archivo_csv, self.medicos)

    def listar_todos(self):
        if not self.medicos:
            print("No hay médicos cargados.")
            return

        print("=" * 70)
        print(f"{'Matrícula':<15} {'Nombre':<30} {'Especialidad':<20}")
        print("-" * 70)
        for m in self.medicos:
            print(f"{m.matricula:<15} {m.nombre:<30} {m.especialidad:<20}")
        print("=" * 70)

    def buscar_por_matricula(self, matricula):
        for m in self.medicos:
            if m.matricula == matricula:
                return m
        return None

    def agregar(self):
        matricula = input("Matrícula: ")
        if self.buscar_por_matricula(matricula):
            print("Ya existe un médico con esa matrícula.")
            return
        nombre = input("Nombre: ")
        especialidad = input("Especialidad: ")
        nuevo = Medico(matricula, nombre, especialidad)
        self.medicos.append(nuevo)
        self.guardar()
        print("Médico agregado.")

    def modificar(self):
        matricula = input("Matrícula a modificar: ")
        medico = self.buscar_por_matricula(matricula)
        if medico:
            nuevo_nombre = input("Nuevo nombre (enter para dejar igual): ")
            nueva_especialidad = input("Nueva especialidad (enter para dejar igual): ")
            if nuevo_nombre:
                medico.nombre = nuevo_nombre
            if nueva_especialidad:
                medico.especialidad = nueva_especialidad
            self.guardar()
            print("Médico modificado.")
        else:
            print("Médico no encontrado.")

    def eliminar(self):
        matricula = input("Matrícula a eliminar: ")
        medico = self.buscar_por_matricula(matricula)
        if medico:
            confirmacion = input(f"¿Está seguro que desea eliminar al médico {medico.nombre} (Matrícula: {matricula})? (S/N): ").strip().upper()
            if confirmacion == "S":
                self.medicos.remove(medico)
                self.guardar()
                print("Médico eliminado.")
            else:
                print("Operación cancelada.")
        else:
            print("Médico no encontrado.")

    def limpiar_pantalla(self):    
        os.system('cls' if os.name == 'nt' else 'clear')

def menu_medicos():
    gestor = GestorDeMedicos()
    gestor.limpiar_pantalla()
    while True:
        

        print("\n" + "="*40)
        print("👨‍⚕️ \033[1mGestión de Médicos\033[0m")
        print("="*40)
        print("[1] Listar todos")
        print("[2] Buscar por matrícula")
        print("[3] Agregar")
        print("[4] Modificar")
        print("\033[31m[5] Eliminar\033[0m") 
        print("[6] Limpiar pantalla")
        print("[7] Exportar CSV")
        print("[0] Volver al menú principal")
        print("="*40)

        opcion = input("Elija una opción: ")
        if opcion == "1":
            gestor.listar_todos()
        elif opcion == "2":
            matricula = input("Matrícula del médico: ")
            medico = gestor.buscar_por_matricula(matricula)
            print(medico if medico else "No encontrado.")
        elif opcion == "3":
            gestor.agregar()
        elif opcion == "4":
            gestor.modificar()
        elif opcion == "5":
            gestor.eliminar()      
        elif opcion == "6":
            gestor.limpiar_pantalla()
        elif opcion == "7":            
            gestor.exportar_datos_csv()
        
        elif opcion == "0":
            gestor.limpiar_pantalla()
            break
        else:
            print("Opción inválida.")