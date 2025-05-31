# -*- coding: utf-8 -*-

import os
from modelos.medico import Medico
from utils.persistencia import Persistencia  
from csv import DictWriter
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
        for m in self.medicos:
            print(m)

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
            self.medicos.remove(medico)
            self.guardar()
            print("Médico eliminado.")
        else:
            print("Médico no encontrado.")

    def limpiar_pantalla(self):    
        os.system('cls' if os.name == 'nt' else 'clear')

def menu_medicos():
    gestor = GestorDeMedicos()
    gestor.limpiar_pantalla()
    while True:
        print("\nGestión de Médicos")
        print("1. Listar todos")
        print("2. Buscar por matrícula")
        print("3. Agregar")
        print("4. Modificar")
        print("5. Eliminar")    
        print("6. Exportar CSV")     
        print("7. Limpiar pantalla")
        print("0. Volver al menú principal")

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
            gestor.exportar_datos_csv()
        elif opcion == "7":
            gestor.limpiar_pantalla()
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")