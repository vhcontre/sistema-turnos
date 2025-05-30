import pickle
import os

class Persistencia:
    """
    Clase utilitaria para la persistencia de datos utilizando el módulo pickle.
    Permite guardar y cargar objetos Python en archivos binarios.

    Métodos:
    --------
    cargar(archivo):
        Carga y retorna los datos almacenados en el archivo especificado.
        Si el archivo no existe o ocurre un error, retorna una lista vacía.

    guardar(archivo, datos):
        Guarda los datos proporcionados en el archivo especificado.
        Si ocurre un error durante el guardado, muestra un mensaje por consola.
    """

    @staticmethod
    def cargar(archivo):
        """
        Carga los datos desde un archivo utilizando pickle.
        'rb' read binary

        Parámetros:
        -----------
        archivo : str
            Ruta del archivo desde donde se cargarán los datos.

        Retorna:
        --------
        datos : object
            Objeto cargado desde el archivo. Si ocurre un error o el archivo no existe, retorna una lista vacía.
        """
        if os.path.exists(archivo):
            with open(archivo, 'rb') as f:
                try:
                    datos = pickle.load(f)
                    return datos
                except Exception as e:
                    print(f"Error al cargar archivo {archivo}: {e}")
                    return []
        else:
            return []

    @staticmethod
    def guardar(archivo, datos):
        """
        Guarda los datos en un archivo utilizando pickle.
        'wb' write binary

        Parámetros:
        -----------
        archivo : str
            Ruta del archivo donde se guardarán los datos.
        datos : object
            Objeto que se desea guardar en el archivo.

        Retorna:
        --------
        None
        """
        try:
            with open(archivo, 'wb') as f:
                pickle.dump(datos, f)
        except Exception as e:
            print(f"Error al guardar archivo {archivo}: {e}")