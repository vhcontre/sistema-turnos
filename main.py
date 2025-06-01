# ==========================================================
# Sistema de Gestión de Turnos Médicos
# Autor: Mónica Rocío Paloqueme
# Carrera: LGTI
# Materia: Algoritmos y Programación
# Profesor: Lucas Frias
# Año: 2025
# ==========================================================

import time
import os
from gestores.gestor_pacientes import menu_pacientes
from gestores.gestor_medicos import menu_medicos
from gestores.gestor_turnos import menu_turnos


def mostrar_inf():
    mensaje = [
        "\n🌟 ¡Felicitaciones, encontraste el huevo de pascua! 🌟",
        "Autor: Mónica Rocío Paloqueme",
        "Agradezco al profesor Lucas Frias por su dedicación y por motivarnos a aprender cada día más. 🙌",
        "¡Sigue programando y nunca dejes de aprender! 🚀\n"
    ]
    for linea in mensaje:
        for c in linea:
            print(c, end='', flush=True)
            time.sleep(0.02)  # velocidad de animación
        print()
        time.sleep(0.3)
    print()
    
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        print("\n" + "="*45)
        print("🏥 \033[1mSistema de Gestión de Turnos Médicos\033[0m")
        print("="*45)
        print("1️⃣  Gestión de Pacientes")
        print("2️⃣  Gestión de Médicos")
        print("3️⃣  Gestión de Turnos")
        print("\033[31m0️⃣  Salir\033[0m")
        print("="*45)

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            menu_pacientes()
        elif opcion == "2":
            menu_medicos()
        elif opcion == "3":
            menu_turnos()
        elif opcion == "0":
            print("Saliendo del Sistema de Gestión de Turnos Médicos.\n")
            break
        elif opcion == "6008":
            mostrar_inf()
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
