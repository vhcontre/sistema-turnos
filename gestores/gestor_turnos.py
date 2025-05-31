# -*- coding: utf-8 -*-

from modelos.turno import Turno
from gestores.gestor_pacientes import GestorDePacientes
from gestores.gestor_medicos import GestorDeMedicos
from utils.persistencia import Persistencia
from utils.fechahora import FechaHora
# from utils.validaciones import es_fecha_valida, es_fecha_futura

class GestorDeTurnos:
    def __init__(self, archivo='datos/turnos.bin'):
        self.archivo = archivo
        self.turnos = Persistencia.cargar(self.archivo)  # <--- usar Persistencia
        self.gestor_pacientes = GestorDePacientes()
        self.gestor_medicos = GestorDeMedicos()

    def guardar(self):
        Persistencia.guardar(self.archivo, self.turnos)  # <--- usar Persistencia

    def listar_todos(self):
        if not self.turnos:
            print("No hay turnos cargados.")
        for t in self.turnos:
            print(t)

    def listar_por_paciente(self, dni):
        encontrados = [t for t in self.turnos if t.paciente_dni == dni]
        if not encontrados:
            print("No se encontraron turnos para ese paciente.")
        for t in encontrados:
            print(t)

    def listar_por_medico(self, matricula):
        encontrados = [t for t in self.turnos if t.medico_matricula == matricula]
        if not encontrados:
            print("No se encontraron turnos para ese médico.")
        for t in encontrados:
            print(t)

    def buscar_por_fecha(self, fecha_hora):
        encontrados = [t for t in self.turnos if t.fecha_hora == fecha_hora]
        if not encontrados:
            print("No se encontraron turnos para esa fecha y hora.")
        for t in encontrados:
            print(t)

    def agregar(self, fecha_hora, paciente_dni, medico_matricula, motivo):
        # Validar fecha y hora        
        if not fecha_hora.es_fecha_futura():
             print("La fecha del turno debe ser futura.")
             return
        
        # Verificar paciente y médico existen
        if not self.gestor_pacientes.buscar_por_dni(paciente_dni):
            print(" Paciente no encontrado.")
            return
        
        if not self.gestor_medicos.buscar_por_matricula(medico_matricula):
            print("Médico no encontrado.")
            return

        # Verificar solapamiento (mismo médico y fecha_hora)
        for t in self.turnos:
            if t.medico_matricula == medico_matricula and t.fecha_hora == fecha_hora:
                print("Ya hay un turno para ese médico a esa fecha y hora.")
                return

        nuevo_turno = Turno(fecha_hora, paciente_dni, medico_matricula, motivo)
        self.turnos.append(nuevo_turno)
        print("Turno agregado.")

    def eliminar(self, fecha_hora, paciente_dni, medico_matricula):
        for t in self.turnos:
            if t.fecha_hora == fecha_hora and t.paciente_dni == paciente_dni and t.medico_matricula == medico_matricula:
                self.turnos.remove(t)
                print("Turno eliminado.")
                return
        print("Turno no encontrado.")

def menu_turnos():
    gestor = GestorDeTurnos()
    while True:
        print("\n📋 Gestión de Turnos")
        print("1. Listar todos")
        print("2. Listar turnos por paciente")
        print("3. Listar turnos por médico")
        print("4. Buscar por fecha y hora")
        print("5. Agregar")
        print("6. Eliminar")
        print("7. Guardar cambios")
        print("0. Volver al menú principal")

        opcion = input("Elija una opción: ")
        if opcion == "1":
            gestor.listar_todos()
        elif opcion == "2":
            dni = input("DNI del paciente: ")
            gestor.listar_por_paciente(dni)
        elif opcion == "3":
            matricula = input("Matrícula del médico: ")
            gestor.listar_por_medico(matricula)
        elif opcion == "4":
            fecha_hora = input("Fecha y hora (dd/mm/aaaa HH:MM): ")
            gestor.buscar_por_fecha(fecha_hora)
        elif opcion == "5":
            fecha_hora_str = input("Fecha y hora (dd/mm/aaaa HH:MM): ")
            fecha_hora = FechaHora.from_string(fecha_hora_str)
            paciente_dni = input("DNI del paciente: ")
            medico_matricula = input("Matrícula del médico: ")
            motivo = input("Motivo del turno: ")
            gestor.agregar(fecha_hora, paciente_dni, medico_matricula, motivo)
        elif opcion == "6":
            fecha_hora = input("Fecha y hora (dd/mm/aaaa HH:MM): ")
            paciente_dni = input("DNI del paciente: ")
            medico_matricula = input("Matrícula del médico: ")
            gestor.eliminar(fecha_hora, paciente_dni, medico_matricula)
        elif opcion == "7":
            gestor.guardar()
            print("Cambios guardados.")
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")
