from datetime import datetime
import re

class Fecha:
    def __init__(self, fecha_str: str = None, hora_str: str = None):
        """
        Si hora_str es None, se asume 00:00.
        Si fecha_str es None, se usa la fecha y hora actual.
        """
        if not fecha_str:
            ahora = datetime.now()
            self.fecha = ahora
        else:
            if not self.es_fecha_valida(fecha_str):
                raise ValueError('Formato de fecha no válido. Debe ser dd/mm/aaaa')
            if not hora_str:
                hora_str = "00:00"
            try:
                self.fecha = datetime.strptime(f"{fecha_str} {hora_str}", "%d/%m/%Y %H:%M")
            except ValueError:
                raise ValueError('Fecha u hora no válida. Verifique el día, mes, año y hora.')

    def es_fecha_valida(self, fecha: str):
        patron = r'^(0[1-9]|[12]\d|3[01])/(0[1-9]|1[0-2])/\d{4}$'
        if not re.match(patron, fecha):
            return False
        try:
            dia, mes, anio = map(int, fecha.split('/'))
            datetime(anio, mes, dia)
            return True
        except Exception:
            return False

    def __str__(self):
        return self.fecha.strftime("%d/%m/%Y %H:%M")

    def __eq__(self, other):
        if isinstance(other, Fecha):
            return self.fecha == other.fecha
        return False

    @classmethod
    def from_string(cls, fecha_hora_str):
        """
        Permite crear una Fecha desde un string 'dd/mm/aaaa HH:MM' o solo 'dd/mm/aaaa'
        """
        partes = fecha_hora_str.strip().split(" ")
        if len(partes) == 2:
            fecha_str, hora_str = partes
        elif len(partes) == 1:
            fecha_str = partes[0]
            hora_str = "00:00"
        else:
            raise ValueError("Formato esperado: 'DD/MM/AAAA HH:MM' o 'DD/MM/AAAA'")
        return cls(fecha_str, hora_str)

    def es_fecha_futura(self):
        return self.fecha > datetime.now()

    def coincide_con(self, otra):
        return self.fecha == otra.fecha