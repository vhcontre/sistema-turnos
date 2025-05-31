# -*- coding: utf-8 -*-

from datetime import datetime

def es_fecha_valida(fecha_str):
    try:
        datetime.strptime(fecha_str, "%d/%m/%Y %H:%M")
        return True
    except ValueError:
        return False

def es_fecha_futura(fecha_str):
    fecha = datetime.strptime(fecha_str, "%d/%m/%Y %H:%M")
    return fecha > datetime.now()
