# -*- coding: utf-8 -*-

import pickle
import os

"""
Utilizo @staticmethod en la clase Persistencia porque los métodos cargar y guardar no dependen de ningún estado interno de la clase ni de la instancia.
Estos métodos solo realizan operaciones generales de lectura y escritura de archivos, por lo que no necesitan acceder a atributos de instancia (self) ni de clase (cls).
Esto hace que el código sea más claro, y los puedo llamar a los métodos directamente desde la clase, sin necesidad de crear el objeto "Persistencia".
"""
class Persistencia:    

    @staticmethod
    def cargar(archivo):
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
        try:
            with open(archivo, 'wb') as f:
                pickle.dump(datos, f)
        except Exception as e:
            print(f"Error al guardar archivo {archivo}: {e}")
    