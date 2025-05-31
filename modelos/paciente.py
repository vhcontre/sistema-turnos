# -*- coding: utf-8 -*-

from utils.fecha import Fecha

class Paciente:
    def __init__(self, dni, nombre, fecha_nacimiento, obra_social=""):
        
        if not isinstance(fecha_nacimiento, Fecha):
            raise TypeError("La fecha de nacimiento debe ser una instancia de la clase Fecha.")
        
        if not dni.isdigit() or len(dni) < 7:
            raise ValueError("El DNI debe ser numérico y tener al menos 7 dígitos.")

        self.dni = dni
        self.nombre = nombre
        self.obra_social = obra_social
        self.fecha_nacimiento = fecha_nacimiento
        

    def __str__(self):
        return f"DNI: {self.dni} | Nombre: {self.nombre} | Obra Social: {self.obra_social} | Nacimiento: {self.fecha_nacimiento}"
