class Turno:
    def __init__(self, fecha_hora, paciente_dni, medico_matricula, motivo):
        self.fecha_hora = fecha_hora  # Instancia de FechaHora
        self.paciente_dni = paciente_dni
        self.medico_matricula = medico_matricula
        self.motivo = motivo

    def __str__(self):
        return f"Turno: {self.fecha_hora} | Paciente DNI: {self.paciente_dni} | Médico Matrícula: {self.medico_matricula} | Motivo: {self.motivo}"
