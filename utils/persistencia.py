# -*- coding: utf-8 -*-

import pickle
import os

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
    