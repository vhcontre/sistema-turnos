from utils.fecha import Fecha

class Turno:
    _ultimo_numero = 0  # Atributo de clase para autoincrementar

    def __init__(self, fecha_hora, paciente_dni, medico_matricula, motivo):
        Turno._ultimo_numero += 1
        self.numero = Turno._ultimo_numero  # Número autoincremental
        self.fecha_hora = fecha_hora  # Instancia de FechaHora
        self.paciente_dni = paciente_dni
        self.medico_matricula = medico_matricula
        self.motivo = motivo
        if not isinstance(self.fecha_hora, Fecha):
            raise TypeError("La fecha_hora del turno debe ser una instancia de la clase FechaHora.")

    def __str__(self):
        return f"Turno N°: {self.numero} | {self.fecha_hora} | Paciente DNI: {self.paciente_dni} | Médico Matrícula: {self.medico_matricula} | Motivo: {self.motivo}"
