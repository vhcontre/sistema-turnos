from datetime import datetime

class FechaHora:
    # def __init__(self, fecha_str, hora_str):
    #     # fecha_str: 'DD/MM/AAAA', hora_str: 'HH:MM'
    #     try:
    #         self.fecha = datetime.strptime(f"{fecha_str} {hora_str}", "%d/%m/%Y %H:%M")
    #     except ValueError:
    #         raise ValueError("Formato de fecha u hora inválido")

    # def __str__(self):
    #     return self.fecha.strftime("%d/%m/%Y %H:%M")
    
    # # Esto solo funcionará si la clase FechaHora implementa correctamente el método __eq__.
    # # Si no lo hace, aunque los valores sean iguales, la comparación == entre dos instancias distintas de FechaHora devolverá False.
    # def __eq__(self, other):
    #     if isinstance(other, FechaHora):
    #         return self.fecha == other.fecha
    #     return False

    # @classmethod
    # def from_string(cls, fecha_hora_str):
    #     try:
    #         fecha_str, hora_str = fecha_hora_str.strip().split(" ")
    #         return cls(fecha_str, hora_str)
    #     except Exception:
    #         raise ValueError("Formato esperado: 'DD/MM/AAAA HH:MM'")

    # def es_fecha_futura(self):
    #     return self.fecha > datetime.now()

    # def coincide_con(self, otra):
    #     return self.fecha == otra.fecha
    pass