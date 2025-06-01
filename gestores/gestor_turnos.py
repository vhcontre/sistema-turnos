# -*- coding: utf-8 -*-

import os
from modelos.turno import Turno
from gestores.gestor_pacientes import GestorDePacientes
from gestores.gestor_medicos import GestorDeMedicos
from utils.persistencia import Persistencia
from utils.fecha import Fecha

class GestorDeTurnos:
    def __init__(self, archivo='datos/turnos.bin'):
        self.archivo = archivo
        self.turnos = Persistencia.cargar(self.archivo)
        if self.turnos:
            Turno._ultimo_numero = max(t.numero for t in self.turnos)
        else:
            Turno._ultimo_numero = 0

        self.gestor_pacientes = GestorDePacientes()
        self.gestor_medicos = GestorDeMedicos()

    def guardar(self):
        Persistencia.guardar(self.archivo, self.turnos)  

    #Parsear significa analizar y convertir una cadena de texto a un formato estructurado.
    def _parsear_fecha_hora(self, fecha_hora_str):
        try:
            partes = fecha_hora_str.strip().split(" ")
            fecha_str, hora_str = partes
            return Fecha(fecha_str, hora_str)
        except Exception:
            raise ValueError("Formato de fecha y hora incorrecto.")

    def listar_todos(self):
        if not self.turnos:
            print("No hay turnos cargados.")
            return
        print("")
        for t in self.turnos:
            print(t)
            print("-" * 100)

    def listar_por_paciente(self):
        dni = input("DNI del paciente: ")
        encontrados = [t for t in self.turnos if t.paciente_dni == dni]
        if not encontrados:
            print("No se encontraron turnos para ese paciente.")
        for t in encontrados:
            print(t)
            print("-" * 80)

    def listar_por_medico(self):
        matricula = input("Matrícula del médico: ")
        encontrados = [t for t in self.turnos if t.medico_matricula == matricula]
        if not encontrados:
            print("No se encontraron turnos para ese médico.")
        for t in encontrados:
            print(t)
            print("-" * 80)

    def buscar_por_fecha(self):
        fecha_hora_str = input("Fecha y hora (dd/mm/aaaa HH:MM): ")
        try:
            fecha_hora = self._parsear_fecha_hora(fecha_hora_str)
        except Exception:
            print("Formato de fecha y hora incorrecto.")
            return
        encontrados = [t for t in self.turnos if t.fecha_hora == fecha_hora]
        if not encontrados:
            print("No se encontraron turnos para esa fecha y hora.")
        for t in encontrados:
            print(t)
            print("-" * 80)

    def agregar(self):
        fecha_hora_str = input("Fecha y hora (dd/mm/aaaa HH:MM): ")
        try:
            fecha_hora = self._parsear_fecha_hora(fecha_hora_str)         
        except Exception:
            print("Formato de fecha y hora incorrecto.")
            return
        if not fecha_hora.es_fecha_futura():
            print("La fecha del turno debe ser futura.")
            return
        paciente_dni = input("DNI del paciente: ")
        if not self.gestor_pacientes.buscar_por_dni(paciente_dni):
            print("Paciente no encontrado.")
            return
        medico_matricula = input("Matrícula del médico: ")
        if not self.gestor_medicos.buscar_por_matricula(medico_matricula):
            print("Médico no encontrado.")
            return
        motivo = input("Motivo del turno: ")
        for t in self.turnos:
            if t.medico_matricula == medico_matricula and t.fecha_hora == fecha_hora:
                print("Ya hay un turno para ese médico a esa fecha y hora.")
                return
        nuevo_turno = Turno(fecha_hora, paciente_dni, medico_matricula, motivo)
        self.turnos.append(nuevo_turno)
        self.guardar()
        print("Turno agregado.")

    def eliminar(self):
        fecha_hora_str = input("Fecha y hora (dd/mm/aaaa HH:MM): ")
        try:
            fecha_hora = self._parsear_fecha_hora(fecha_hora_str)
        except Exception:
            print("Formato de fecha y hora incorrecto.")
            return
        paciente_dni = input("DNI del paciente: ")
        medico_matricula = input("Matrícula del médico: ")
        for t in self.turnos:
            if t.fecha_hora == fecha_hora and t.paciente_dni == paciente_dni and t.medico_matricula == medico_matricula:
                confirmacion = input(f"¿Está seguro que desea eliminar el turno de {paciente_dni} con el médico {medico_matricula} en {fecha_hora}? (S/N): ").strip().upper()
                if confirmacion == "S":
                    self.turnos.remove(t)
                    self.guardar()
                    print("Turno eliminado.")
                else:
                    print("Operación cancelada.")
                return
        print("Turno no encontrado.")
    
    def limpiar_pantalla(self):    
        os.system('cls' if os.name == 'nt' else 'clear')
        
def menu_turnos():
    gestor = GestorDeTurnos()
    gestor.limpiar_pantalla()  
    while True:        

        print("\n" + "="*40)
        print("📒 \033[1mGestión de Turnos\033[0m")
        print("="*40)
        print("[1] Listar todos")
        print("[2] Listar turnos por paciente")
        print("[3] Listar turnos por médico")
        print("[4] Buscar por fecha y hora")
        print("[5] Agregar")
        print("\033[31m[6] Eliminar\033[0m") 
        print("[7] Limpiar pantalla")
        print("[0] Volver al menú principal")
        print("="*40)

        opcion = input("Elija una opción: ")
        if opcion == "1":
            gestor.listar_todos()
        elif opcion == "2":
            gestor.listar_por_paciente()
        elif opcion == "3":
            gestor.listar_por_medico()
        elif opcion == "4":
            gestor.buscar_por_fecha()
        elif opcion == "5":
            gestor.agregar()
        elif opcion == "6":
            gestor.eliminar()
        elif opcion == "7":
            gestor.limpiar_pantalla()
        elif opcion == "0":
            gestor.limpiar_pantalla()
            break
        else:
            print("Opción inválida.")