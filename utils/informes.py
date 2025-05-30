# -*- coding: utf-8 -*-

from collections import Counter

def contar_turnos_por_medico(turnos):
    contador = Counter()
    for turno in turnos:
        contador[turno.medico_matricula] += 1
    return dict(contador)
