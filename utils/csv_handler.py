import csv

def exportar_csv(nombre_archivo, lista_objetos):
    if not lista_objetos:
        print("No hay datos para exportar.")
        return
    # Convierte cada objeto a dict
    lista_dict = [vars(obj) for obj in lista_objetos]
    claves = lista_dict[0].keys()
    with open(nombre_archivo, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=claves)
        writer.writeheader()
        writer.writerows(lista_dict)
    print(f"Datos exportados a {nombre_archivo}")

def importar_csv(nombre_archivo):
    with open(nombre_archivo, newline='') as archivo:
        reader = csv.DictReader(archivo)
        return list(reader)
