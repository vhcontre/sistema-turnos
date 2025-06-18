#file: utils/csv_handler.py
import csv

def exportar_csv(nombre_archivo, lista_objetos):
    """
    Exporta una lista de objetos a un archivo CSV.

    Parámetros:
    -----------
    nombre_archivo : str
        Ruta y nombre del archivo CSV de destino.
    lista_objetos : list
        Lista de objetos (por ejemplo, instancias de una clase) a exportar.
        Cada objeto se convierte a un diccionario usando vars(obj).

    Funcionamiento:
    ---------------
    - Si la lista está vacía, muestra un mensaje y no exporta nada.
    - Convierte cada objeto a un diccionario.
    - Usa los nombres de los atributos como encabezados del CSV.
    - Escribe los datos en el archivo CSV especificado.
    """
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
    """
    Importa datos desde un archivo CSV y los devuelve como una lista de diccionarios.

    Parámetros:
    -----------
    nombre_archivo : str
        Ruta y nombre del archivo CSV a importar.

    Retorna:
    --------
    list
        Lista de diccionarios, donde cada diccionario representa una fila del CSV.
    """
    with open(nombre_archivo, newline='') as archivo:
        reader = csv.DictReader(archivo)
        return list(reader)