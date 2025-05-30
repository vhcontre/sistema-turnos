# -*- coding: utf-8 -*-

from gestores.gestor_pacientes import menu_pacientes
from gestores.gestor_medicos import menu_medicos

def main():
    while True:
        print("\n🏥 Sistema de Gestión de Turnos Médicos")
        print("1. Gestión de Pacientes")
        print("2. Gestión de Médicos")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            menu_pacientes()
        elif opcion == "2":
            menu_medicos()
        elif opcion == "0":
            print("👋 Saliendo...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()