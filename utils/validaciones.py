# -*- coding: utf-8 -*-

from datetime import datetime

def es_fecha_futura(fecha_hora_str):
    try:
        fecha = datetime.strptime(fecha_hora_str, "%d/%m/%Y %H:%M")
        return fecha > datetime.now()
    except ValueError:
        return False
