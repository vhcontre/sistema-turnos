from gestores.gestor_pacientes import GestorDePacientes

def menu_pacientes():
    gestor = GestorDePacientes()
    while True:
        print("\n📋 Gestión de Pacientes")
        print("1. Listar todos")
        print("2. Buscar por DNI")
        print("3. Agregar")
        print("4. Modificar")
        print("5. Eliminar")
        print("6. Guardar cambios")
        print("0. Volver al menú principal")

        opcion = input("Elija una opción: ")
        if opcion == "1":
            gestor.listar_todos()
        elif opcion == "2":
            dni = input("DNI del paciente: ")
            paciente = gestor.buscar_por_dni(dni)
            print(paciente if paciente else "No encontrado.")
        elif opcion == "3":
            dni = input("DNI: ")
            nombre = input("Nombre: ")
            fecha = input("Fecha de nacimiento (dd/mm/aaaa): ")
            obra = input("Obra social (opcional): ")
            gestor.agregar(dni, nombre, fecha, obra)
        elif opcion == "4":
            dni = input("DNI a modificar: ")
            nombre = input("Nuevo nombre (enter para dejar igual): ")
            obra = input("Nueva obra social (enter para dejar igual): ")
            fecha = input("Nueva fecha de nacimiento (dd/mm/aaaa o enter): ")
            gestor.modificar(dni,
                             nuevo_nombre=nombre if nombre else None,
                             nueva_obra_social=obra if obra else None,
                             nueva_fecha=fecha if fecha else None)
        elif opcion == "5":
            dni = input("DNI a eliminar: ")
            gestor.eliminar(dni)
        elif opcion == "6":
            gestor.guardar()
            print("Cambios guardados.")
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu_pacientes()