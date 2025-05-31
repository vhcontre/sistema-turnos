import os
from gestores.gestor_pacientes import menu_pacientes
from gestores.gestor_medicos import menu_medicos
from gestores.gestor_turnos import menu_turnos

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        print("\nSistema de Gestión de Turnos Médicos")
        print("1. Gestión de Pacientes")
        print("2. Gestión de Médicos")
        print("3. Gestión de Turnos")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            menu_pacientes()
        elif opcion == "2":
            menu_medicos()
        elif opcion == "3":
            menu_turnos()
        elif opcion == "0":
            print("Saliendo.")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
