# -*- coding: utf-8 -*-
import pickle
import os
from modelos.medico import Medico

class GestorDeMedicos:
    def __init__(self, archivo='datos/medicos.bin'):
        self.archivo = archivo
        self.medicos = []
        self.cargar()

    def cargar(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, 'rb') as f:
                self.medicos = pickle.load(f)
        else:
            self.medicos = []

    def guardar(self):
        with open(self.archivo, 'wb') as f:
            pickle.dump(self.medicos, f)

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

    def agregar(self, matricula, nombre, especialidad):
        if self.buscar_por_matricula(matricula):
            print("Ya existe un médico con esa matrícula.")
            return
        nuevo = Medico(matricula, nombre, especialidad)
        self.medicos.append(nuevo)
        print("Médico agregado.")

    def modificar(self, matricula, nuevo_nombre=None, nueva_especialidad=None):
        medico = self.buscar_por_matricula(matricula)
        if medico:
            if nuevo_nombre:
                medico.nombre = nuevo_nombre
            if nueva_especialidad:
                medico.especialidad = nueva_especialidad
            print("Médico modificado.")
        else:
            print("Médico no encontrado.")

    def eliminar(self, matricula):
        medico = self.buscar_por_matricula(matricula)
        if medico:
            self.medicos.remove(medico)
            print("Médico eliminado.")
        else:
            print("Médico no encontrado.")

def menu_medicos():
    gestor = GestorDeMedicos()
    while True:
        print("\n📋 Gestión de Médicos")
        print("1. Listar todos")
        print("2. Buscar por matrícula")
        print("3. Agregar")
        print("4. Modificar")
        print("5. Eliminar")
        print("6. Guardar cambios")
        print("0. Volver al menú principal")

        opcion = input("Elija una opción: ")
        if opcion == "1":
            gestor.listar_todos()
        elif opcion == "2":
            matricula = input("Matrícula del médico: ")
            medico = gestor.buscar_por_matricula(matricula)
            print(medico if medico else "No encontrado.")
        elif opcion == "3":
            matricula = input("Matrícula: ")
            nombre = input("Nombre: ")
            especialidad = input("Especialidad: ")
            gestor.agregar(matricula, nombre, especialidad)
        elif opcion == "4":
            matricula = input("Matrícula a modificar: ")
            nombre = input("Nuevo nombre (enter para dejar igual): ")
            especialidad = input("Nueva especialidad (enter para dejar igual): ")
            gestor.modificar(matricula,
                             nuevo_nombre=nombre if nombre else None,
                             nueva_especialidad=especialidad if especialidad else None)
        elif opcion == "5":
            matricula = input("Matrícula a eliminar: ")
            gestor.eliminar(matricula)
        elif opcion == "6":
            gestor.guardar()
            print("Cambios guardados.")
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")
